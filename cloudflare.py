#!/usr/bin/python
import socket

subdomainlist = ["ftp", "cpanel", "webmail", "localhost", "local", "mysql", "forum", "driect-connect", "blog", "vb", "forums", "home", "direct", "forums", "mail", "access", "admin", "administrator", "email", "downloads", "ssh", "owa","bbs", "webmin", "paralel", "parallels", "www0", "www", "www1", "www2", "www3", "www4", "www5","shop", "api", "blogs", "test","mx1","cdn", "mysql", "mail1", "secure", "server", "ns1", "ns2", "smtp", "vpn", "m", "mail2", "postal", "support", "web", "dev"]

print (" ")
print (''' \033[91m   _____  _     _____ _   _____________ _       ___  ______ _____  \033[0m''')
print (''' \033[91m  /  __ \| |   |  _  | | | |  _  \  ___| |     / _ \ | ___ \  ___| \033[0m''')
print (''' \033[91m  | /  \/| |   | | | | | | | | | | |_  | |    / /_\ \| |_/ / |__   \033[0m''')
print (''' \033[91m  | |    | |   | | | | | | | | | |  _| | |    |  _  ||    /|  __|  \033[0m''')
print (''' \033[91m  | \__/\| |___\ \_/ / |_| | |/ /| |   | |____| | | || |\ \| |___  \033[0m''')
print (''' \033[91m   \____/\_____/\___/ \___/|___/ \_|   \_____/\_| |_/\_| \_\____/  \033[0m''')
print (" ")

print (''' \033[93m [*] Sample Web Site : google.com  \033[0m''') 
host = raw_input(''' \033[92m [*] Enter Website Address : \033[0m''')
print (" ")

for sublist in subdomainlist:
    try:
       hosts = str(sublist) + "." + str(host)
       showip = socket.gethostbyname(str(hosts))
       print "   [+] CloudFlare Bypass "+str(showip)+' | '+str(hosts)
    except:
            pass
        
