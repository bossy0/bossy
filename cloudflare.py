#!/usr/bin/python
import socket

subdomainlist = ["mail", "direct", "direct-connect", "direct-connect-mail", "cpanel", "ftp", "ntp", "forum", "forums", "blog", "dev", "web", "webmail", "record", "ssl", "help", "development", "mysql", "admin", "pop", "imap", "beta", "portal", "m", "java", "server", "client", "ts3", "swf", "id", "ads", "images", "news", "alerts", "ap", "db", "backup", "pbx", "upload", "vpn", "ldap", "apps", "secure", "chat", "alpha", "local", "crs", "cvs" "cms", "corp", "home", "test", "smtp", "ssh", "citrix", "wiki", "*A", "mobile", "www", "www1", "www2", "www3", "www4", "www5", "www6", "www7", "www8", "www9", "www10", "www11", "www12", "www13", "www14", "www15", "www16", "www17", "www18", "www19", "www20", "dns", "dns1", "dns2", "dns3", "dns4", "dns5", "dns6", "dns7", "dns8", "dns9", "dns10", "dns11", "dns12", "dns13", "dns14", "dns15", "dns16", "dns17", "dns18", "dns19", "dns20", "ns", "ns1", "ns2", "ns3", "ns4", "ns5", "ns6", "ns7", "ns8", "ns9", "ns10", "ns11", "ns12", "ns13", "ns14", "ns15", "ns16", "ns17", "ns18", "ns19", "ns20", "ipv", "ipv1", "ipv2", "ipv3", "ipv4", "ipv5", "ipv6", "ipv7", "ipv8", "ipv9", "ipv10", "ipv11", "ipv12", "ipv13", "ipv14", "ipv15", "ipv16","ipv17", "ipv18", "ipv19", "ipv20", ]

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
       print "  [+] CloudFlare Resolver "+str(showip)+' | '+str(hosts)
    except:
            pass
        
