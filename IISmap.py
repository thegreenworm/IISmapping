import gmplot
import os
import urllib.request
import json
import time
import webbrowser




count = 0
latList = []
longList = []
while(count <3):
    http = urllib.request.urlopen('http://api.open-notify.org/iss-now.json')
    # response = http.request(self,'GET','http://api.open-notify.org/iss-now.json')
    result = json.loads(http.read())
    lat = float(result['iss_position']['latitude'])
    long = float(result['iss_position']['longitude'])
    latList.append(lat)
    longList.append(long)
    print(latList)
    print(longList)
    time.sleep(7)
    count += 1

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