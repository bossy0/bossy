#!/usr/bin/env python
import socket
from multiprocessing.dummy import Pool as ThreadPool
import sys
from datetime import datetime
from time import strftime

# Clear the screen
# subprocess.call('cls', shell=True)

# Ask for input
remoteServer    = raw_input("\033[94m > [*] Enter Target IP Adress : \033[0m")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print "\033[91m- \033[0m" * 56
print "\033[91m > [*] Please Wait Scanning Remote Host \033[0m", remoteServerIP
print "\033[91m- \033[0m" * 56
print "\033[93m > [*] Scanning Started At \033[0m" + strftime("%H:%M:%S") + " ! "

t1 = datetime.now()

def scan(ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServerIP, ports))
    if result == 0:
        byte = str.encode("Server:\r\n")
        sock.send(byte)
        banner = sock.recv(1024)
        print "\033[92m > [*] Port {} : Open \033[0m".format(ports)

# function to be mapped over
def scanParallel(ports, threads=8):
    pool = ThreadPool(threads)
    results = pool.map(scan, ports)
    pool.close()
    pool.join()
    return results

if __name__ == "__main__":
    ports =(21,22,23,53,80,443,3306,8080)
    results = scanParallel(ports, 8)
    
    t2 = datetime.now()
    total =  t2 - t1
    
# Printing the information to screen
print "\033[93m > [*] Scanning Finished At \033[0m" + strftime("%H:%M:%S") + " . . ."
print '\033[93m > [*] Scanning Completed In : \033[0m', total
