'''
Created on 2015年3月9日
拿來當server端用的
@author: weiwei
'''
import http.client

class Subwait:
    def __init__(self,host,channel):
        self.host = host
        self.channel = channel
        self.answer = ""
    def stayThere(self):
        conn = http.client.HTTPConnection(self.host)
        conn.request('GET','/sub/'+ self.channel)
        response = conn.getresponse()
        self.answer = response.read()
        return self.answer

