#!/usr/bin/env python3
#coding = utf-8
'''
pure push channel test for NginX push Module
NginX Push Stream Module: https://github.com/wandenberg/nginx-push-stream-module
SUB: curl -s -v 'http://10.78.78.88/sub/978'
PUB: curl -s -v -X POST 'http://10.78.78.88/pub?id=978' -d 'Hello_Kitty'
'''

import http.client, urllib.request, urllib.parse, threading, requests

host = "10.78.78.88"
channel = "978"
messageIndex="test"
messageText="ok"
"""
class SubWait(threading.Thread):
	def __init__(self, host, channel):
		super(SubWait, self).__init__()
		self.host = host
		self.channel = channel
		self.subresp = ""
	def SubInfo(self):
		'''
		#settings = { 'interval': '0', 'count':'1' }
		url = 'http://10.78.78.88/sub/978'
		#r = requests.get(url, params=settings, stream=True)
		r = requests.get(url)
		for line in r.iter_lines():
			if line:
				print(line)
		return(line)'''
		conn = http.client.HTTPConnection(self.host)
		conn.request('GET', '/sub/'+self.channel)
		resp = conn.getresponse()
		self.subresp = resp.read()
		return(self.subresp)
"""
class PubData(threading.Thread):
	def __init__(self, host, channel):
		super(PubData, self).__init__()
		self.host = host
		self.channel = channel
		self.pubresp = ""
	def PubInfo(self):
		conn = http.client.HTTPConnection(self.host)
		params = urllib.parse.urlencode({"test":"OK"})
		conn.request('POST', '/pub?id='+channel, params)
		resp = conn.getresponse()
		#return(resp.status, resp.reason)
		self.pubresp = resp.read()
		return(conn.request)
		conn.close()


#SubWait(host, channel).start()
PubData(host, channel).start()
