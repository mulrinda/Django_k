# 네이버 프로필 이미지 크롤링

import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=bts'
res = requests.get(url).content.decode()
soup = BeautifulSoup(res, 'html.parser')

#imgs = soup.find_all('div', class_='member_thumb')
# imgs = soup.find("img", attrs={"data-value": True})

# imgs = soup.find("img", attrs={"alt":"가수 방탄소년단 이미지"})
imgs = soup.find_all("img", attrs={"alt":True})[1]['src']
print(imgs)

    #member_thumb> a:nth-child(1) > img