# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:27:14 2019

@author: Luke Nguyen
"""

import requests
from bs4 import BeautifulSoup
import html.parser


# Grab URL from website
URL = "https://sandiego.craigslist.org/d/apts-housing-for-rent/search/apa"
r = requests.get(URL)

# Parse HTML
soup = BeautifulSoup(r.text, 'html.parser')

for link in soup.find_all('a', {'class': 'result-title hdrlnk'}):
    
    print (link['href'])
