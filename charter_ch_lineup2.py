# -*- coding: utf-8 -*-
import re, urllib2
from time import sleep
from contextlib import closing
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# Open Firefox to charter using Selenium
browser = Firefox()
browser.get('https://www.charter.com/browse/content/new-channel-lineup')

# Click the "choose state" menu using Selenium
wait = WebDriverWait('browser', 20)
button = browser.find_element_by_css_selector('.drop-down-current')
button.click()

# Identify all states in the list, read as text using Selenium, then print
list_item = browser.find_element_by_class_name('drop-down-list')
states = list_item.text
print "States: " + states
print
# Give time to load all states
print "Waiting..."
sleep(3)
print "CLEAR!"
print


# Find specific state using Selenium
find_st = browser.find_element_by_link_text('MI')
cur_state = find_st.text
print cur_state
find_st.click()


def scraps():
    text_str = st.readlines()
    # print st
    states_list = list(st)
    # print states_list



# left off here, trying to organize states list as a list() so each list item will have a number id






page_source = browser.page_source
##print page_source

# browser.close()