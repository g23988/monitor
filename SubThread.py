'''
Created on 2015年3月9日
處發多執行蓄
@author: weiwei
'''
import threading,Subserver
class hostThread (threading.Thread):
    def __init__(self,threadID, host, channel):
        threading.Thread.__init__(self)
        self.host = host
        self.channel = channel
    def run(self):
        serverconn = Subserver.Subwait(self.host,self.channel)
        a = serverconn.stayThere()
        return a
