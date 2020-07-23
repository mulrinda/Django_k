import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import pandas as pd

html="""<p>응봉산(해발 94m)에서 바라보는 일출은 한강과 서울숲, 잠실운동장 등 서울 동부권의 모습을 한눈에 볼 수 있다. 한강조망명소로 사진 작가 및 많은 이들이 찾고 있으며, 매년 1월 1일 해맞이 행사를 실시한다. 또한, 개나리꽃의 명소이기도 한 응봉산에서는 4월경 개나리 축제를 열고 있다.<br></p>
"""
# 1) reqeusts 라이브러리를 활용한 HTML 페이지 요청 
# 1-1) res 객체에 HTML 데이터가 저장되고, res.content로 데이터를 추출할 수 있음
res = requests.get('https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid=fcf0e335-6e67-4520-83de-517f9e6b7778')
print(res.content)
