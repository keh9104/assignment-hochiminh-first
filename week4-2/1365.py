from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get('https://1365.go.kr/vols/P9210/partcptn/timeCptn.do')

data = driver.page_source
soup = BeautifulSoup(data, 'html.parser')

for i in soup('em'):
    i.decompose()

notices = soup.find_all(class_='tit_board_list')


for n in notices:
    print(n.text.strip())
