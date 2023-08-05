from bs4 import BeautifulSoup
import urllib.request
import re


search_term = "housing bubble"
search_url = "http://www.wikihow.com/" + \
    'wikiHowTo?search='+urllib.parse.quote(search_term)
content = urllib.request.urlopen(search_url)

content = urllib.request.urlopen(search_url)
read_content = content.read()
soup = BeautifulSoup(read_content, 'html.parser').findAll('a', attrs={'class': 'result_link'})[0]

img = soup.find('div', {'class': 'result_thumb'})
style_attr = img.get('style')
url = style_attr.split('url(')[1].split(')')[0]


result_data = soup.find('div', {'class': 'result_data'})
title = result_data.find('div',{'class': 'result_title'}).text
views = result_data.find('li', {'class': 'sr_view'}).text.strip()
update = result_data.find('li', {'class': 'sr_updated'}).text
update = update[:8].lstrip()+" "+update[8:].lstrip()
sp_verif = result_data.find('li', {'class': 'sp_verif'}).text.strip()


print(url)
print(title)
print(views)
print(update)
print(sp_verif)
