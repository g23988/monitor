#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
pure push channel test for NginX push Module
NginX Push Stream Module: https://github.com/wandenberg/nginx-push-stream-module
SUB: curl -s -v 'http://10.78.78.88/sub/978'
PUB: curl -s -v -X POST 'http://10.78.78.88/pub?id=978' -d 'Hello_Kitty'
'''

import http.client, urllib.request, urllib.parse, threading, requests

host = "10.78.78.88"
channel = "978"
content = {channel:"OK"}

class SUBSCRIBE(threading.Thread):
	def __init__(self, threadID):
		threading.Thread.__init__(self)
		self.threadID = threadID
	def run(self):
		subconn = http.client.HTTPConnection(host)
		subconn.request('GET', '/sub/'+channel)
		subresp = subconn.getresponse()
		subdata = subresp.read()
		return(subdata)

def PUBLISH():
	pubconn = http.client.HTTPConnection(host)
	pubparams = urllib.parse.urlencode(content)
	pubconn.request('POST', '/pub?id='+channel, pubparams)
	pubresp = pubconn.getresponse()
	#print(pubresp.status, pubresp.reason)
	pubdata = pubresp.read()
	return(pubdata.strip())
	pubconn.close()

threadLock = threading.Lock()
threads = []
SubThread = SUBSCRIBE(1)
SubThread.start()

#count = 0

while(SubThread.isAlive()):
	PUBLISH()
#	if subdata == pubdata.strip():

#	count+=1
#	print(str(count))

SubThread.join()