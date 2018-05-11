import requests
nList= []
nProxL = ''
file = open('proxy.txt')
for line in file:
    try:
        aproxy = line.strip('\n')
        user_agent = {'User-agent': 'Mozilla/5.0'}
        print aproxy
        proxies = {
            "http": aproxy
            }
        r = requests.get("http://www.google.com", proxies=proxies, headers=user_agent, timeout=1)
        aproxy = aproxy + " \n"
        nList.append(aproxy)
        nProxL = ''.join(nList)
        f = open('WorkingProxy.txt', 'w')
        f.write(nProxL)
        f.close()
        print aproxy, " Added"
    except Exception, e:
        print "Connection Error ", e
file.close()
print "Proxy list cleaned and updated!"
