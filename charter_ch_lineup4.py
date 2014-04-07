# -*- coding: utf-8 -*-

from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from pygeocoder import Geocoder
import pygmaps
import gmaps2

# Open Firefox to charter using Selenium
browser = Firefox()
browser.get('https://www.charter.com/browse/content/new-channel-lineup')

# Click the "choose state" menu using Selenium
wait = WebDriverWait('browser', 20)
button = browser.find_element_by_css_selector('.drop-down-current')
button.click()

# # Identify all states in the list, read as text using Selenium
list_item = browser.find_element_by_class_name('drop-down-list')
states = list_item.text

# sel_st = raw_input('Type in 2 letter st abbreviation: ')
find_st = browser.find_element_by_link_text('MI')
find_st.click()
sleep(1)
list_region = browser.find_element_by_xpath('//*[@id="select-region"]/div[2]') # find and click Choose Region button
list_region.click()
cur_state = browser.find_element_by_xpath('//*[@id="select-region"]/div[3]')

# text_region = cur_state.find_elements_by_tag_name('a') # find all regions by <a> tag
l_regions = cur_state.text

print "l_regions"
print l_regions
# creates text file with all the region
regions = open('Regions.text', 'w+')
regions.write(l_regions)
sleep(3.0)


# Place region points on map
# gmaps2.gmaps_mapit(l_regions)

def gmaps_mapit():
    # f = open('Regions.text', 'r')
    # map_regions = []
    # for line in f:
    #     map_regions.append(line.rstrip('\n'))

    # print state
    regions_map = pygmaps.maps(44.3148443, -85.60236429999999,7) # Generate state map
    f = open('Regions.text', 'r')
    map_regions = []
    for line in f:
        map_regions.append(line.rstrip('\n'))
    print "map_regions"
    print map_regions

    def geo_region():
        for item in map_regions:
            try:
                geo = Geocoder.geocode(item)
            except:
                pass
            else:
                point = (geo[0].coordinates)
                title = item
                joint = ', '.join(map(str, point))
                split_point = joint.split(',', 2)
                lat = split_point[0]
                lon = split_point[1]
                if '(All Digital)' in item:
                    regions_map.addpoint(float(lat), float(lon), "#0101DF", title=title)
                else:
                    regions_map.addpoint(float(lat), float(lon), "#FF0000", title=title)

            # print "Point: "
            # print point
            # print "Joint: "
            # print joint
            # print "split_joint: "
            # print split_point

            sleep(0.1)

    geo_region()

    regions_map.draw('./mymap.html')
    print "Done"

gmaps_mapit()

# url = './mymap.html'
# webbrowser.open_new_tab(url)

browser.close()