from django.test import TestCase
import requests
from bs4 import BeautifulSoup
import csv

# 네이버 프로필 이미지 크롤링

f = open('csv/singer/singerMember.csv', 'r', encoding='utf-8')
fw = open('csv/singer/singerMember2.csv','w', encoding='utf-8')
rdf = csv.reader(f)
wr = csv.writer(fw)
count=1
for line in rdf:
    # print(line[1])   # type = list
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query='+line[1]
    res = requests.get(url).content.decode()
    soup = BeautifulSoup(res, 'html.parser')
    imgs = soup.find_all("img", attrs={"alt":True})[1]['src']
    print(imgs)
    wr.writerow([count,imgs,True])
    #imgs = soup.find_all('div', class_='member_thumb')
    # imgs = soup.find("img", attrs={"data-value": True})
    count += 1
    # imgs = soup.find("img", attrs={"alt":"가수 방탄소년단 이미지"})
f.close()
fw.close()
    #member_thumb> a:nth-child(1) > img