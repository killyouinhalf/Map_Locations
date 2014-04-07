__author__ = 'digital1'

from pygeocoder import Geocoder
import pygmaps
import time

# generate list of all regions
# def gmaps_mapit():
#     regions_map = pygmaps.maps(44.3148443, -85.60236429999999,7) # Generate state map
#     f = open('Regions2.text', 'r')
#     map_regions = []
#     for line in f:
#         map_regions.append(line.rstrip('\n'))
#     print map_regions
#
#     def geo_region():
#         for item in map_regions:
#             try:
#                 geo = Geocoder.geocode(item)
#             except:
#                 pass
#             else:
#                 point = (geo[0].coordinates)
#                 title = item
#                 joint = ', '.join(map(str, point))
#                 split_point = joint.split(',', 2)
#                 lat = split_point[0]
#                 lon = split_point[1]
#                 if '(All Digital)' in item:
#                     regions_map.addpoint(float(lat), float(lon), "#0101DF", title=title)
#                 else:
#                     regions_map.addpoint(float(lat), float(lon), "#FF0000", title=title)
#
#             # print "Point: "
#             # print point
#             # print "Joint: "
#             # print joint
#             # print "split_joint: "
#             # print split_point
#
#             time.sleep(0.1)
#
#     geo_region()
#
#     regions_map.draw('./mymap.html')
#
# gmaps_mapit()




