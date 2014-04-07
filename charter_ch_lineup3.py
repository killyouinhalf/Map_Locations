# -*- coding: utf-8 -*-

from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from pygeocoder import Geocoder
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
find_st = browser.find_element_by_link_text('CO')
find_st.click()
sleep(1)
list_region = browser.find_element_by_xpath('//*[@id="select-region"]/div[2]') # find and click Choose Region button
list_region.click()
cur_state = browser.find_element_by_xpath('//*[@id="select-region"]/div[3]')

# text_region = cur_state.find_elements_by_tag_name('a') # find all regions by <a> tag
l_regions = cur_state.text

# creates text file with all the region
regions = open('Regions.text', 'w')
regions.write(l_regions)

print l_regions
# Place region points on map
gmaps2.gmaps_mapit(l_regions)


# url = './mymap.html'
# webbrowser.open_new_tab(url)

browser.close()