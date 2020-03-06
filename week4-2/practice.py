from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query='
plusUrl = input('띠를 입력하세요(쥐, 소, 호랑이, 토끼, 용, 뱀, 말, 양, 원숭이, 닭, 개, 돼지): ')
lastUrl = '띠%20운세'
url = baseUrl + quote_plus(plusUrl) + lastUrl

driver = webdriver.Chrome()
driver.get(url)


html = driver.page_source
soup = BeautifulSoup(html)

search = soup.find(class_="text _cs_fortune_text")

print(search)

driver.close
