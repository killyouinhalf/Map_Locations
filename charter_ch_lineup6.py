# -*- coding: utf-8 -*-

from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pygeocoder import Geocoder
import pygmaps
from bs4 import BeautifulSoup



browser = Firefox()
browser.get('https://www.charter.com/browse/content/new-channel-lineup')
wait = WebDriverWait('browser', 20)
button = browser.find_element_by_css_selector('.drop-down-current')
button.click()
list_item = browser.find_element_by_class_name('drop-down-list')
# states = list_item.text
# print states


while True:
    st_prompt = raw_input("Enter 2 letter state abbreviation: ")
    find_st = browser.find_element_by_link_text(st_prompt.upper())
    sel_st = find_st.text + ', USA'
    print sel_st
    find_st.click() # click to sel state
    sleep(1)
    try:
        list_region = WebDriverWait(browser, 02).until(EC.visibility_of((By.ID, "select-region")))
        # list_region = browser.find_element_by_xpath('//*[@id="select-region"]/div[2]') # find Choose Region button
        list_region.click()
        print "Success!"
        break
    else:
        print "No Charter!"

print "Moving on..."
cur_state = browser.find_element_by_xpath('//*[@id="select-region"]/div[3]')







# text_region = cur_state.find_elements_by_tag_name('a') # find all regions by <a> tag
def temp():
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
