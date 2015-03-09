#!/usr/bin/env python3
#coding = utf-8
'''
 pure push channel test for NginX push Module
NginX Push Stream Module: https://github.com/wandenberg/nginx-push-stream-module
SUB: curl -s -v 'http://10.78.78.88/sub/978'
PUB: curl -s -v -X POST 'http://10.78.78.88/pub?id=978' -d 'Hello_Kitty'
'''
import time, itertools
import http.client, urllib.request, urllib.parse, Subserver, threading, SubThread
host = '192.168.25.135'
channel = '978'
messageIndex="test"
messageText="ok"
#現誠上鎖

tStart = time.time()

threadLock = threading.Lock()
threads = []
thread1 = SubThread.hostThread("thread1",host,channel)
thread1.start()


#重是記數器
count = 0
#狂拳連打
print("發動技能!狂拳連打")
while(thread1.isAlive()):
    conn = http.client.HTTPConnection(host)
    params = urllib.parse.urlencode({messageIndex:messageText})
    conn.request('POST', '/pub?id='+channel, params)
    count =count+1
    print(str(count)+" Combo!")
#print(resp.status, resp.reason)
thread1.join()
resp = conn.getresponse()
data = resp.read()
print(data.strip())
print("連續打擊"+str(count)+"次")
tStop = time.time()
print(tStop - tStart)
conn.close()