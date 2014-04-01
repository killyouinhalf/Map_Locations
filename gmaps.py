__author__ = 'digital1'

import pygmaps
import webbrowser
from pygeocoder import Geocoder
import time

def gmaps_test():
    print "(gmaps test)"

def gmaps_mapit():
    f = open('states.txt', 'r')
    states = []
    for line in f:
        states.append(line.rstrip('\n'))
    print states

    home = "Home"
    st_coords = []
    def geo_state():
        for st in states:
            geo = Geocoder.geocode(st)
            point = (geo[0].coordinates)
            st_coords.append(point)
            time.sleep(0.5)
            print st_coords

    geo_state()



    mymap = pygmaps.maps(45.0702432, -85.2653517, 14)
    loc = mymap.addpoint(45.0702432, -85.2653517, "#0000FF")
    print loc
    loc2 = mymap.addpoint(45.0702032, -85.2652117, "#FF0000")
    print loc2
    # mymap.addpoint{
    #     'loc_01' : '45.0702436, -85.2653512, "#00FF00"',
    #     'loc_02' : '245.0702439, -85.2653516, "#00FF00"',
    #     'loc_03' : '45.0702432, -85.2653519, "#00FF00"'
    # }

    mymap.draw('./mymap.html')
    url = './mymap.html'
    webbrowser.open_new_tab(url)



gmaps_mapit()




import urllib2

from geopy.geocoders import GoogleV3

# geolocator = GoogleV3()
# address, (latitude, longitude) = geolocator.geocode("Traverse City, MI")
# print (address, latitude, longitude)





