import os
import requests
from bs4 import BeautifulSoup
from string import punctuation
punctuation = punctuation.replace("'", "")
num = int(input())
type = input()
my_dir = os.getcwd()


def request(u):
    r = requests.get(u, headers={'Accept-Language': 'en-US,en;q=0.5'}).content
    return BeautifulSoup(r, 'html.parser')


for i in range(num):
    os.mkdir('Page_' + str(i + 1))
    os.chdir('Page_' + str(i + 1))
    url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=' + str(i + 1)
    soup = request(url)
    all_articles_main = soup.find_all('article')
    for article in all_articles_main:
        if article.find('span', class_='c-meta__type').text == type:
            all_articles = request('https://www.nature.com' + article.find('a', class_='c-card__link u-link-inherit').get('href'))
            header = all_articles.find('h1').text
            table = header.maketrans('', '', punctuation)
            head = header.translate(table).replace(' ', '_')
            final = open((head + '.txt'), 'w', encoding='utf8')
            body = all_articles.find('div', class_='c-article-body u-clearfix')
            if body is None :
                body = all_articles.find('div', class_='article-item__body')
            for i in body :
                try :
                    final.write(i.text)
                except AttributeError :
                    continue
            final.close()
    os.chdir(my_dir)