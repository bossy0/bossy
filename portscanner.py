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

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors

def scan(ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServerIP, ports))
    if result == 0:
        byte = str.encode("Server:\r\n")
        sock.send(byte)
        banner = sock.recv(2500)
        print "[*] Port {} : Open".format(ports)

# function to be mapped over
def scanParallel(ports, threads=2500):
    pool = ThreadPool(threads)
    results = pool.map(scan, ports)
    pool.close()
    pool.join()
    return results

if __name__ == "__main__":
    ports =(21,22,23,53,80,443,3306,8080)
    results = scanParallel(ports, 2500)

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print "[*] Scanning Finished At " + strftime("%H:%M:%S") + "!"
print '[*] Scanning Completed In : ', total
