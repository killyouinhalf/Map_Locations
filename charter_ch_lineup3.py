# -*- coding: utf-8 -*-
# import re
# import urllib
from time import sleep
import gmaps
from contextlib import closing
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from googlemaps import GoogleMaps
# from selenium.webdriver.support import expected_conditions as EC

gmaps.gmaps_test()

# Open Firefox to charter using Selenium
browser = Firefox()
browser.get('https://www.charter.com/browse/content/new-channel-lineup')
# sleep(5)

# Click the "choose state" menu using Selenium
wait = WebDriverWait('browser', 20)
button = browser.find_element_by_css_selector('.drop-down-current')
button.click()

# Identify all states in the list, read as text using Selenium, then print
list_item = browser.find_element_by_class_name('drop-down-list')
states = list_item.text
print ("States list: " + states)
print()
# Give time to load all states
print ("Waiting...")
sleep(3)
print ("CLEAR!")
print()


# Find specific state using Selenium
find_st = browser.find_element_by_link_text('MI')
cur_state = find_st.text
print (cur_state)
find_st.click()

gmaps.gmaps_mapit()

browser.close()