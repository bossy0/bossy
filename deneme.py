import urllib2
import sys
import threading
import random
import re
import time
import socket
socket.setdefaulttimeout(1)
#global params
url=''
host=''
headers_useragents=[]#87
headers_referers=[]#159
keyword_top=[]#24
request_counter=100000
flag=0
safe=0
