# -*- coding: utf-8 -*-
import urllib
from BeautifulSoup import *

url = raw_input('Enter -')

html = urllib.urlopen(url).read() # string containing the whole web page

# Print page as plain text
# print '--------------------'
# print html
# print '--------------------'

soup = BeautifulSoup(html) # make sense of all the html data... It is the parsed HTML data, like a "soup" object. 

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML atributes

tags = soup('a') # Find all the tags <a> ... </a>, Kind of like a dictionary
# <a> is refered as "anchor tabs"

for tag in tags:
	print tag.get('href', None) # Once we have preselected all <a..>, we look for the href items.
