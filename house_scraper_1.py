# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:27:14 2019

@author: Luke Nguyen
"""

import requests
from bs4 import BeautifulSoup
import html.parser
import pandas as pd


# Grab URL from website
#URL = "https://sandiego.craigslist.org/d/apts-housing-for-rent/search/apa"
#r = requests.get(URL)

# Parse HTML
#soup = BeautifulSoup(r.text, 'html.parser')

#    for house in soup.find_all('a', {'class': 'result-title hdrlnk'}):
#        house_URL= house['href']
#        r = requests.get(URL)
#        house_post = BeautifulSoup(r.text, 'html.parser')

#house = soup.find('a', {'class': 'result-title hdrlnk'})
house.URL = house['href']

r = requests.get(house.URL)
house_post = BeautifulSoup(r.text, 'html.parser')
house.address = house_post.find('div', {'class': 'mapaddress'})
house.lattitude = house_post.find('div', {'id': 'map'})
house.longitude = house_post.find('div', {'id': 'map'})['data-longitude']
print(house_post.latitude)



