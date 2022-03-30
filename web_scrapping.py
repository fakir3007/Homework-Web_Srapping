import requests
from  bs4 import BeautifulSoup

DATA_URL = 'https://habr.com/ru/all'
KEYWORDS = ['дизаин', 'фото', 'web', 'python']
SOURCE = requests.get(DATA_URL).text

soup = BeautifulSop(SOURCE, 'lxml')

for article in soup.find_all('article'):
    headline = article.h2.a.text
    post_preview_text = article.div.div.text
    post_link = article.find('a', class_='post_title_link').get('href')
    public_date = article.find('span', class_='post_time').text

    for search_word in KEYWORDS:
        if(search_word.lower() in headline.lower()) or (search_word.lower() in post_preview_text.lower()):
            print(f'Дата: {public_date} - Заголовок:{headline} - Ссылка:{post_link}')