__author__ = 'digital1'


from pygeocoder import Geocoder
import pygmaps
import time
#
# def gmaps_test():
#     print "(gmaps test)"
#
# try:
#   address = Geocoder.geocode('NY, NY')
# except GeocoderError:
#   print "The address entered could not be geocoded"
#   sys.exit(1)
#
# if not address.valid_address:
#   print "The address entered is not valid, but we did get some info"
#
# address_test = Geocoder.geocode("Arnold Lake/Hayes, MI (All Digital)")
# if address_test.valid_address:
#     print "Sweet"

# generate list of all regions
def gmaps_mapit():
    regions_map = pygmaps.maps(44.3148443, -85.60236429999999,7) # Generate state map
    f = open('Regions2.text', 'r')
    map_regions = []
    for line in f:
        map_regions.append(line.rstrip('\n'))
    print map_regions

    region_coords = []
    def geo_region():
        for item in map_regions:
            try:
                geo = Geocoder.geocode(item)
            except:
                pass
            else:
                point = (geo[0].coordinates)
                joint = ', '.join(map(str, point))
                split_point = joint.split(',', 2)
                lat = split_point[0]
                lon = split_point[1]
            print point # point represents the lat/long for each city
            # print split_joint
        #     print lats
        #     print lons
        regions_map.addpoint(float(lat), float(lon))
        #         region_coords.append(joint)
        #         time.sleep(0.5)
        # print region_coords


        # for x in region_coords:
        #     map_coords()
        #     mymap = pygmaps.maps(45.0702432, -85.2653517, 14)
        #     mymap.addpoint(45.0702432, -85.2653517, "#0000FF")
        #     mymap.addpoint(45.0702032, -85.2652117, "#FF0000")

    geo_region()



    # regions_map.addpoint(44.3148443, -85.60236429999999)
    def map_coords():
        for x in region_coords:
            regions_map.addpoint(x)
            # regions_map.addpoint(44.3148443, -85.60236429999999)





    map_coords()

    regions_map.draw('./mymap.html')



gmaps_mapit()




import urllib2

from geopy.geocoders import GoogleV3

# geolocator = GoogleV3()
# address, (latitude, longitude) = geolocator.geocode("Traverse City, MI")
# print (address, latitude, longitude)





