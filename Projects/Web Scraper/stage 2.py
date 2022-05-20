import requests
from bs4 import BeautifulSoup
url = input('Input the URL: ')
r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
soup = BeautifulSoup(r.content, 'html.parser')
title =  soup.find('h1')
description = soup.find('span', {'data-testid': 'plot-l'})

if 'https://www.imdb.com/title/' in url:
    print({"title" : title.text, "description" : description.text})
else:
    print('Invalid movie page!')