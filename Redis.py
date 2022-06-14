import redis
import gmplot
import os
import urllib.request
import json
from urllib3 import response
import time

r = redis.Redis(host='localhost', port=6379, db=0)
count = 1

while count < 1000000:
    
    http = urllib.request.urlopen('http://api.open-notify.org/iss-now.json')
    result = json.loads(http.read())
    r.set(str(count),'{},{}'.format(result['iss_position']['latitude'],result['iss_position']['longitude']))
    r.expire(str(count),40)
    redisGet = str(r.get(str(count)))
    # print(redisGet)
    s = redisGet.strip("b''")
    print("key: " + str(count) + "  " + s)
    count += 1
    time.sleep(7)

   




# string = r.keys("*")
# count = 0
# newlist = []
# for aaaa in string:
#     badstuff = str(aaaa)
#     x = badstuff.strip("b''")
#     # x = badstuff.replace("b'","")
#     # x = x.replace("'","")
#     x= int(x)
#     newlist.append(x)
#     print(x)
#     count +=1
# print(newlist)




