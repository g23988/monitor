#!/usr/bin/env python3
#coding = utf-8
'''
 pure push channel test for NginX push Module
NginX Push Stream Module: https://github.com/wandenberg/nginx-push-stream-module
SUB: curl -s -v 'http://10.78.78.88/sub/978'
PUB: curl -s -v -X POST 'http://10.78.78.88/pub?id=978' -d 'Hello_Kitty'
'''

import http.client,urllib.request, urllib.parse

host = '192.168.25.135'
channel = '978'
messageIndex="test"
messageText="ok"

conn = http.client.HTTPConnection(host)
params = urllib.parse.urlencode({'messageText':'messageText'})
conn.request('POST', '/pub?id='+channel, params)
resp = conn.getresponse()
#print(resp.status, resp.reason)
data = resp.read()
print(data.strip())
conn.close()