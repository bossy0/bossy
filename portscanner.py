#!/usr/bin/env python
import socket
from multiprocessing.dummy import Pool as ThreadPool
import sys
from datetime import datetime
from time import strftime

# Clear the screen
# subprocess.call('cls', shell=True)

# Ask for input
remoteServer    = raw_input("\033[1;36m > [*] Enter Target IP Adress : \033[1;m")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print "\033[91m = \033[0m" * 18
print "\033[91m > [*] Please Wait Scanning Remote Host \033[0m", remoteServerIP
print "\033[91m = \033[0m" * 18
print "\033[93m > [*] Scanning Started At \033[0m" + strftime("\033[93m %H:%M:%S \033[0m") + "\033[93m ! \033[0m"

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
def scanParallel(ports, threads=135):
    pool = ThreadPool(threads)
    results = pool.map(scan, ports)
    pool.close()
    pool.join()
    return results

if __name__ == "__main__":
    ports =(21,22,23,25,53,80,110,115,135,139,143,194,443,445,465,587,993,995,1433,25565,3306,3389,5432,5900,6112,8080,8443)
    results = scanParallel(ports, 135)
    
    t2 = datetime.now()
    total =  t2 - t1
    
# Printing the information to screen
print "\033[93m > [!] Scanning Finished At \033[0m" + strftime("\033[93m %H:%M:%S \033[0m") + "\033[93m . . . \033[0m"
print '\033[93m > [!] Scanning Completed \033[0m'
