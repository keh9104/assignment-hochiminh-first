import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
query = input('뉴스 검색: ')

fullurl = url + query

data = requests.get(fullurl).text
soup = BeautifulSoup(data, 'html.parser')
news_title = soup.find_all(class_='_sp_each_title')
title_array = []

for title in news_title:
    title_array.append(title.get('title'))

print(title_array)
