import requests
from bs4 import BeautifulSoup
import pandas

base_url = 'http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/'

data_list =[]

for page in range(0, 30, 10):
    new_base_url = f'{base_url}t=0&s={page}.html'

    r = requests.get(f"{new_base_url}", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

    c = r.content 

    soup = BeautifulSoup(c, 'html.parser')

    property_data = soup.find_all('div', {'class': 'propertyRow'})

    # first_property = property_data[0].find('h4', {'class': 'propPrice'}).text.replace('\n', '').replace(' ','')

    # print(first_property)

    # print(type(first_property))

    for item in property_data:
        d = {}

        d['Price'] = item.find('h4', {'class': 'propPrice'}).text.replace('\n', '').replace(' ','')
        d['City'] = item.find_all('span', {'class': 'propAddressCollapse'})[0].text
        d['Address'] = item.find_all('span', {'class': 'propAddressCollapse'})[1].text
        try:
            d['Beds'] = item.find('span', {'class': 'infoBed'}).text
        except: 
            d['Beds'] = None
        try:
            d['Area'] = item.find('span', {'class': 'infoSqFt'}).text
        except: 
            d['Area'] =  None
        try:
            d['Full Bath'] = item.find('span', {'class': 'infoValueFullBath'}).text
        except: 
            d['Full Bath'] =  None
        try: 
            d['Half Bath'] = item.find('span', {'class': 'infoValueHalfBath'}).text
        except: 
            d['Half Bath'] =  None
        
        for column_group in item.find_all('div', {'class': 'columnGroup'}):
            for feature_group, feature_name in zip(column_group.find_all('span', {'class': 'featureGroup'}), column_group.find_all('span', {'class': 'featureName'})):
                if 'Lot size' in feature_group:
                    print(feature_name.text)

        data_list.append(d)

df = pandas.DataFrame(data_list)

print(df)

# df.to_csv('property_data')



