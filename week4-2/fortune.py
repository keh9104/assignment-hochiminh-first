import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query='
query = input('오늘의 운세! *띠를 입력하세요(쥐, 소, 호랑이, 토끼, 용, 뱀, 말, 양, 원숭이, 닭, 개, 돼지): ')
lasturl = '띠%20운세'

fullurl = url + query + lasturl

data = requests.get(fullurl).text
soup = BeautifulSoup(data, 'html.parser')

fortune = soup.find(class_="text _cs_fortune_text")
print(fortune)

'''
news_title = soup.find_all(class_='_sp_each_title')
title_array = []

for title in news_title:
    title_array.append(title.get('title'))

print(title_array)
'''
