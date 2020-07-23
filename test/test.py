from bs4 import BeautifulSoup
import pandas as pd
import requests


# 1) reqeusts 라이브러리를 활용한 HTML 페이지 요청 
# 1-1) res 객체에 HTML 데이터가 저장되고, res.content로 데이터를 추출할 수 있음
res = requests.get('https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=fcf0e335-6e67-4520-83de-517f9e6b7778')
# print(res.content)
# 2) HTML 페이지 파싱 BeautifulSoup(HTML데이터, 파싱방법)
# 2-1) BeautifulSoup 파싱방법
# soup = BeautifulSoup(res.content, 'html.parser')
# title = soup.find_all('resultInfo')
# print("title은"+title)

bs = BeautifulSoup(res, 'lxml')
result = bs.find_all('img')
#print(result)
#print(str(result))
#result2 = bs.find_all('span', class_="additional-name")
#print(result2)
#print(len(result2))
#print(type(table))
print(result)
# results = []
# results2 = []
# a = 0
# for data in result:
#     #print(data)
#     a = a + 1
#     results2.append(a)
#     results.append(data)

# #print(results)
# #print(type(results))

# data = pd.DataFrame([results, results2])
# print(type(data))
# #print(data)
# data.to_csv('C:/Users/i9i91/OneDrive/바탕 화면/github 저장내용/portfolio.io/크롤링22.csv')  




