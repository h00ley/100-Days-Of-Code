import requests
from bs4 import BeautifulSoup

url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
all_articles_main = soup.find_all('span', {'class': 'c-meta__type'}, text="News")


for article in all_articles_main:
    all_articles = article.find_parent('article').find('a', {'data-track-action': 'view article'})
    links = 'https://www.nature.com' + all_articles.get("href")
    title = all_articles.text
    new_title = title.replace(" ", "_")
    r2 = requests.get(links)
    soup2 = BeautifulSoup(r2.content, 'html.parser')
    article_body = soup2.find('div', {'class' : "c-article-body"}).text.strip()
    file = open(f'{new_title}.txt', 'w', encoding='utf-8')
    file.write(article_body)
    file.close()
    print('Content saved.')
