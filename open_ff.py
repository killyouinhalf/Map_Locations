# -*- coding: utf-8 -*-
__author__ = 'digital1'

from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait

def ff():
    browser = Firefox()
    browser.get('https://www.charter.com/browse/content/new-channel-lineup')
    wait = WebDriverWait('browser', 20)

    button = browser.find_element_by_xpath('//*[@id="select-state"]/div[2]') # find and click Choose State button
    button.click()

list_item = browser.find_element_by_xpath('//*[@id="select-state"]/div[3]/ul') #