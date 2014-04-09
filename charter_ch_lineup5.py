# -*- coding: utf-8 -*-

from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from pygeocoder import Geocoder
import pygmaps


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
# print states

# sel_st = raw_input('Type in 2 letter st abbreviation: ')


while True:
    st_prompt = raw_input("Enter 2 letter state abbreviation: ") # enter state
    find_st = browser.find_element_by_link_text(st_prompt.upper())
    sel_st = find_st.text + ', USA'
    print sel_st
    find_st.click() # click to sel state
    sleep(1)
    list_region = browser.find_element_by_xpath('//*[@id="select-region"]/div[2]') # find Choose Region button
    check_region = list_region.text
    if check_region:
        print "No Charter!"
    else:
        list_region.click()
        break
cur_state = browser.find_element_by_xpath('//*[@id="select-region"]/div[3]')

# text_region = cur_state.find_elements_by_tag_name('a') # find all regions by <a> tag
l_regions = cur_state.text

print "l_regions: "
print l_regions
# creates text file with all the region
regions = open('Regions.text', 'w+')
# regions.write("Come on!" '\n')
regions.write(l_regions)
sleep(3.0)
regions.close()
browser.close()

# open_browser()

# def gmaps_mapit(self):
print "GO!"
# f = open('Regions.text', 'r')
# map_regions = []
# for line in f:
#     map_regions.append(line.rstrip('\n'))

geo = Geocoder.geocode(self.sel_st)
geo_st = (geo[0].coordinates)
st_joint = ', '.join(map(str, geo_st))
split_st_joint = st_joint.split(',', 2)
st_lat = split_st_joint[0]
st_lon = split_st_joint[1]
print st_joint
print split_st_joint
print st_lat
print st_lon
regions_map = pygmaps.maps(float(st_lat), float(st_lon),7) # Generate state map
f = open('Regions.text', 'r')
map_regions = []
for line in f:
    map_regions.append(line.rstrip('\n'))
print "map_regions: "
print map_regions

def geo_region():
    for item in map_regions:
        try:
            geo_reg = Geocoder.geocode(item)
        except:
            pass
        else:
            point = (geo_reg[0].coordinates)
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

# gmaps_mapit()

go = map_charter()
go.open_browser()
go.gmaps_mapit()

    # url = './mymap.html'
    # webbrowser.open_new_tab(url)

    # browser.close()