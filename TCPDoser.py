import time
import socket
import random
import threading

print '''
╔╦╗╔═╗╔═╗  ╔╦╗╔═╗╔═╗╔═╗╦═╗
 ║ ║  ╠═╝───║║║ ║╚═╗║╣ ╠╦╝
 ╩ ╚═╝╩    ═╩╝╚═╝╚═╝╚═╝╩╚═ '''
time.sleep(0.5)
print (" ")
ip = raw_input("IP : ")
port = input("Port : ")
thread_num = input("Threads : ")
