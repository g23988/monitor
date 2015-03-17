'''
Created on 2015年3月17日

@author: weiwei
'''
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
pure push channel test for NginX push Module
NginX Push Stream Module: https://github.com/wandenberg/nginx-push-stream-module
SUB: curl -s -v 'http://10.78.78.88/sub/978'
PUB: curl -s -v -X POST 'http://10.78.78.88/pub?id=978' -d 'Hello_Kitty'
'''

import http.client, urllib.request, urllib.parse, threading

host = "192.168.25.135"
channel = "978"
content = {channel:"OK"}
getresult = ''


class SUBSCRIBE(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        global getresult
        subconn = http.client.HTTPConnection(host)
        subconn.request('GET', '/sub/'+channel)
        subresp = subconn.getresponse()
        subdata = str(subresp.read())
        getresult = subdata
#        return(subdata)

def PUBLISH():
    pubconn = http.client.HTTPConnection(host)
    pubparams = urllib.parse.urlencode(content)
    pubconn.request('POST', '/pub?id='+channel, pubparams)
    pubresp = pubconn.getresponse()
    #print(pubresp.status, pubresp.reason)
    pubdata = pubresp.read()
    return(pubdata.strip())
    pubconn.close()


#threadLock = threading.Lock()
#threadLock.acquire()
#threads = []
SubThread = SUBSCRIBE(1)
print('啟動server')
SubThread.start()
print('送出post')
PUBLISH()
SubThread.join()
#a = str(getresult)
#type(a)
while (True):
    #print(type(getresult))
    if getresult == "b'978=OK'":
        print('比對正常')
        break
print('ㄧ切安好!!!!!!!!!!!!')
#count = 0




#while(SubThread.isAlive()):
#    print('123')
#    PUBLISH()
#    if subdata == pubdata.strip():

#    count+=1
#    print(str(count))
