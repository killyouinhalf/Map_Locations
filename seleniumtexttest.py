__author__ = 'digital1'


import selenium

goopen = open('states.txt', 'r')
read = goopen.read()
sel_text = read.text
states = list_item.text