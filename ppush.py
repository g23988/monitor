import redis, pprint, os
from redis.client import Redis
from types import GetSetDescriptorType
from nt import remove
r = Redis(host='192.168.25.135',port=6379,db=0)


for dirPath, dirNames, fileNames in os.walk("./src/"):
    for f in fileNames:
        onsend = open("./src/"+f)
        onsendtext = onsend.read()
        r.rpush('filename',f)
        r.rpush('text',onsendtext)
        onsend.close()
        remove("./src/"+f)
        
        
print r.llen('filename')



swit = True

while swit:
    if r.llen('filename')==0:
        swit=False
    else:
        getsent = open("./dst/"+r.lpop('filename'),'w')
        getsenttext = r.lpop('text')
        getsent.write(getsenttext)
        getsent.close()
        
#getsent = r.get('testa.html')('foo',onsendtext)
