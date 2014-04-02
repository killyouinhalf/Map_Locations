# -*- coding: utf-8 -*-


from time import sleep
from open_ff import *

ff()


print open_ff.list_item
states = list_item.text
print states
# ass = list_item.split('\n')
# print ass
#
# sleep(1)
#
# find_st = browser.find_element_by_link_text('MI')
# find_st.click()
# sleep(1)
#
# list_region = browser.find_element_by_xpath('//*[@id="select-region"]/div[2]')
# list_region.click()
# cur_state = browser.find_element_by_xpath('//*[@id="select-region"]/div[3]')
# l_regions = cur_state.text
# butt = l_regions.split('\n')
# print butt


def gmaps_mapit():
    print ("Mapping it!")
    # f = open('regions', 'r')
    map_regions = []
    for line in l_regions:
        map_regions.append('\n')
    print map_regions

    # home = "Home"
    # st_coords = []
    # def geo_state():
    #     for st in states:
    #         geo = Geocoder.geocode(st)
    #         point = (geo[0].coordinates)
    #         st_coords.append(point)
    #         time.sleep(0.5)
    #         print st_coords
    #
    # geo_state()
    #
    #
    #
    # mymap = pygmaps.maps(45.0702432, -85.2653517, 14)
    # loc = mymap.addpoint(45.0702432, -85.2653517, "#0000FF")
    # print loc
    # loc2 = mymap.addpoint(45.0702032, -85.2652117, "#FF0000")
    # print loc2
    # # mymap.addpoint{
    # #     'loc_01' : '45.0702436, -85.2653512, "#00FF00"',
    # #     'loc_02' : '245.0702439, -85.2653516, "#00FF00"',
    # #     'loc_03' : '45.0702432, -85.2653519, "#00FF00"'
    # # }
    #
    # mymap.draw('./mymap.html')
    # url = './mymap.html'
    # webbrowser.open_new_tab(url)



# gmaps_mapit()




# browser.close()