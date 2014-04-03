# -*- coding: utf-8 -*-
import re
# import urllib
from time import sleep
# import gmaps
from contextlib import closing
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from pygeocoder import Geocoder
from googlemaps import GoogleMaps
# from selenium.webdriver.support import expected_conditions as EC

# gmaps.gmaps_test()

# Open Firefox to charter using Selenium
browser = Firefox()
browser.get('https://www.charter.com/browse/content/new-channel-lineup')
# browser.get('https://www.yahoo.com')

# sleep(5)
#
# Click the "choose state" menu using Selenium
wait = WebDriverWait('browser', 20)
button = browser.find_element_by_css_selector('.drop-down-current')
button.click()
#
# # Identify all states in the list, read as text using Selenium, then print
list_item = browser.find_element_by_class_name('drop-down-list')
states = list_item.text
# ass = list_item.split('\n')
# print ass
# print ("States list: " + states)
# print()
# # Give time to load all states
# print ("Waiting...")
# sleep(1)
# print ("CLEAR!")
# print()
#
#
# # Find specific state using Selenium
# sel_st = raw_input('Type in 2 letter st abbreviation: ')
find_st = browser.find_element_by_link_text('MI')
find_st.click()
sleep(1)

list_region = browser.find_element_by_xpath('//*[@id="select-region"]/div[2]') # find and click Choose Region button
list_region.click()
cur_state = browser.find_element_by_xpath('//*[@id="select-region"]/div[3]')

# text_region = cur_state.find_elements_by_tag_name('a') # find all regions by <a> tag
l_regions = cur_state.text
# print l_regions
# print list(l_regions)

# creates text file with all the region
regions = open('Regions.text', 'w')
regions.write(l_regions)


# Place region points on map
# gmaps.gmaps_mapit()
# def gmaps_test():
#     print "(gmaps test)"

def gmaps_mapit():
    # print ("Mapping it!")
    # map_regions = []
    # for line in l_regions:
    #     map_regions.append(line)
    # print map_regions


    st_coords = []
    def geo_state():
        for line in l_regions:
            geo = Geocoder.geocode(line)
            point = (geo[0].coordinates)
            st_coords.append(point)
            sleep(0.5)
        print st_coords

    geo_state()
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