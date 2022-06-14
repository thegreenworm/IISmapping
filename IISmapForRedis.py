import gmplot
import os
import urllib.request
import json
import time
import webbrowser
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

string = r.keys("*")
count = 0
keyList = []
for aaaa in string:
    badstuff = str(aaaa)
    x = badstuff.strip("b''")
    # x = badstuff.replace("b'","")
    # x = x.replace("'","")
    x= int(x)
    keyList.append(x)
    print(x)
    count +=1
keyList.sort()
print(keyList)


newCount = 0
index = keyList[newCount]
latList = []
longList = []
while(newCount <= 4):
    try:
        result = str(r.get(index))
        resultStrip = result.strip("b''")
        print(resultStrip)
        # lat = float(result['iss_position']['latitude'])
        # long = float(result['iss_position']['longitude'])
        newCount += 1
        # if newCount == 3:
        #     newCount = 0
        #     continue
        print("index before: " + str(index))
        index = keyList[newCount]
        print("index after: " + str(index))
        resultSplit = resultStrip.split(",")
        lat = resultSplit[0]
        long = resultSplit[1]
        latList.append(float(lat))
        longList.append(float(long))
        print(latList)
        print(longList)
    except IndexError as e:
        index = keyList[0]
        # newCount = 0
        # continue

heatLat = [latList[0]]
heatLong = [longList[0]]

# gmap = gmplot.GoogleMapPlotter(40.758480,-111.888138,13)
gmap3 = gmplot.GoogleMapPlotter(latList[1], 
                                longList[1], 10) 

gmap3.scatter(latList,longList,
                    '#FF0000', size=300,marker=False)
gmap3.plot(latList,longList,
                'cornflowerblue',edge_width=2.5)
gmap3.heatmap(heatLat,heatLong)

if os.path.exists("map.html"):
    os.remove('map.html')
    
    gmap3.draw("map.html")
    webbrowser.open_new_tab('map.html')
else:
    gmap3.draw("map.html")
    webbrowser.open_new_tab('map.html')