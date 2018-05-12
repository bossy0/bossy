#!/usr/bin/env python
import socket
from multiprocessing.dummy import Pool as ThreadPool
import sys
from datetime import datetime
from time import strftime

# Clear the screen
# subprocess.call('cls', shell=True)

# Ask for input
remoteServer    = raw_input("[*] Enter Target IP Adress : ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print "-" * 56
print "[*] Please Wait Scanning Remote Host", remoteServerIP
print "-" * 56
print "[*] Scanning Started At " + strftime("%H:%M:%S") + "!"

def scan(ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServerIP, ports))
    if result == 0:
        byte = str.encode("Server:\r\n")
        sock.send(byte)
        banner = sock.recv(1024)
        print "[*] Port {} : Open".format(ports)

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

# Printing the information to screen
print "[*] Scanning Finished At " + strftime("%H:%M:%S") + "!"
