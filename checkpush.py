#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
Created on 2015年3月17日

@author: weiwei
'''


'''
pure push channel test for NginX push Module
NginX Push Stream Module: https://github.com/wandenberg/nginx-push-stream-module
SUB: curl -s -v 'http://10.78.78.88/sub/978'
PUB: curl -s -v -X POST 'http://10.78.78.88/pub?id=978' -d 'Hello_Kitty'
'''

import http.client, urllib.request, urllib.parse, threading, os, sys


host = "192.168.25.135"
channel = "978"
content = {host:channel}
getresult = b''
flag = True
#Lock
mylock = threading.RLock()





class SUBSCRIBE(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        try:
            global getresult
            global flag
            subconn = http.client.HTTPConnection(host,80,timeout=1)
            subconn.request('GET', '/sub/'+channel)
            mylock.acquire()
            #改變flag
            flag = False
            subresp = subconn.getresponse()
            subdata = subresp.read()
            getresult = subdata
            mylock.release()
        except:
            return Exception
        finally:
            subconn.close()

def PUBLISH():
    pubconn = http.client.HTTPConnection(host)
    pubparams = urllib.parse.urlencode(content)
    pubconn.request('POST', '/pub?id='+channel, pubparams)
    pubconn.close()

try:
    
    SubThread = SUBSCRIBE(1)
    print('啟動server')
    SubThread.start()
    #等到sub被建立以後才送出post
    while True:
        if flag == False:  
            print('送出post')
            PUBLISH()
            break
    
    while True:
        if getresult.decode('UTF-8') == host+"="+channel:
            print('比對正常')
            break
    print('流程完成')
except EOFError:
    print(EOFError)
    #print('錯誤連線,請檢察參數')




