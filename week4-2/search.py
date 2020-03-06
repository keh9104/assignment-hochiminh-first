import requests
from bs4 import BeautifulSoup

url = input("검색하고 싶은 페이지를 적어 주세요 (ex: www.xxx.com):")
response = requests.get('https://' + url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
