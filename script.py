import requests
from bs4 import BeautifulSoup

# Scaping data from Sky Sports - Premier League Table 

r = requests.get("https://www.skysports.com/premier-league-table", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

c = r.content

page = BeautifulSoup(c, 'html.parser')

page.prettify()

table = page.find_all('tr', {'class': 'standing-table__row'})[1:]

prem_table = []

for i in table:
    position = i.find_all('td', {'class': 'standing-table__cell'})[0].text
    team = i.find_all('a', {'class': 'standing-table__cell--name-link'})[0].text
    prem_table.append({'position': position, 'team': team})

print(prem_table[5])

# Scaping Data from original lecture 

# c = r.content
# soup = BeautifulSoup(c, 'html.parser')

# cities = soup.find_all('div', {'class': 'cities'})

# new_cities = []
# for i in cities:
#     h2 = i.find_all('h2')[0].text
#     p = i.find_all('p')[0].text
#     new_cities.append({'city': h2, 'information': p})

# print(new_cities)