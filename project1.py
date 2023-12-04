import requests as req
from bs4 import BeautifulSoup

url = "https://ria.ru/"
r = req.get(url)
soup = BeautifulSoup(r.text, 'lxml')
news = soup.find_all('span', class_ = 'cell-list__item-title')
time = soup.find_all('div', class_ = 'cell-info__date')

for i in range(0, len(news)):
    print(news[i].text + ".")
    tex = "Опубликовано"
    print(f'{tex: >30}', time[i].text)
    print(" ")