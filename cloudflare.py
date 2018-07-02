#!/usr/bin/python
import socket

subdomainlist = ["mail", "direct", "direct-connect", "direct-connect-mail", "cpanel", "ftp", "forum", "blog", "dev", "webmail", "record", "ssl", "dns", "help", "www", "admin", "pop", "imap", "beta", "portal", "m", "java", "server", "client", "ts3"]

print (" ")
print (''' \033[91m   _____  _     _____ _   _____________ _       ___  ______ _____  \033[0m''')
print (''' \033[91m  /  __ \| |   |  _  | | | |  _  \  ___| |     / _ \ | ___ \  ___| \033[0m''')
print (''' \033[91m  | /  \/| |   | | | | | | | | | | |_  | |    / /_\ \| |_/ / |__   \033[0m''')
print (''' \033[91m  | |    | |   | | | | | | | | | |  _| | |    |  _  ||    /|  __|  \033[0m''')
print (''' \033[91m  | \__/\| |___\ \_/ / |_| | |/ /| |   | |____| | | || |\ \| |___  \033[0m''')
print (''' \033[91m   \____/\_____/\___/ \___/|___/ \_|   \_____/\_| |_/\_| \_\____/  \033[0m''')
print (''' \033[91m '---------------------------------------------------------------' \033[0m''')
print (''' \033[91m |      /facebook.com/bossy.078   /instagram.com/bossy.078       | \033[0m''')
print (''' \033[91m '---------------------------------------------------------------' \033[0m''')
print (" ")

print (" \033[1;33m [*] Sample Website : google.com \033[1;m") 
print (" ")
host    = raw_input("\033[1;36m  [*] Enter Website Address : \033[1;m")
print (" ")

for sublist in subdomainlist:
    try:
       hosts = str(sublist) + "." + str(host)
       showip = socket.gethostbyname(str(hosts))
       print "  [+] CloudFlare Bypass "+str(showip)+' | '+str(hosts)
    except:
            pass
        
