import requests
from bs4 import BeautifulSoup 
import pandas
import re

base_url = 'https://www.zoopla.co.uk/for-sale/property/northampton/?identifier=northampton&q=Northampton%2C%20Northamptonshire&search_source=home&radius=0&pn='

r = requests.get(f'{base_url}1', headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

c = r.content

soup = BeautifulSoup(c, 'html.parser')

property_data = soup.find_all('div', {'class': 'listing-results-wrapper'})

property_list = []

# print(property_data[0].find('span', {'class': 'num-beds'}).text)

def average_dist_trainstation (loc_1, loc_2):
    return sum(loc_1, loc_2) / 2

for prop in property_data:

    d = {}

    d['Location'] = prop.find('a', {'class': 'listing-results-address'}).text
    d['Price'] = prop.find('a', {'class': 'listing-results-price'}).text.replace('\n', '').replace(' ', '')
    try:
        d['Bedrooms'] = prop.find('span', {'class': 'num-beds'}).text
    except:
        d['Bedrooms'] = None
    try:
        d['Bathrooms'] = prop.find('span', {'class': 'num-baths'}).text
    except:
        d['Bathrooms'] = None
    try:
        d['Living-room'] = prop.find('span', {'class': 'num-reception'}).text
    except:
        d['Living-room'] = None
    
    if 'Guide' not in prop.find('a', {'class': 'listing-results-price'}).text:
            property_list.append(d)


property_data_pandas = pandas.DataFrame(property_list)

print(property_data_pandas)