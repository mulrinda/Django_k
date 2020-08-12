from django.shortcuts import render
from urllib.parse import urlparse
import pandas as pd
import json
import requests

def goods(request):
    return render(request,'tothers/goods.html')

def tourtip(request):
    return render(request,'tothers/tourtip.html')

def stamp(request):
    return render(request,'tothers/stamp.html')

def theme(request,cont,lang):
    url='tothers/theme_'+cont+'_'+lang+'.html'
    return render(request, url)

# 카카오로 위경도 받아올때 참고하려고 index에 넣어놓음. addr에 주소변경하면 실행할때 터미널에 위경도 뜸
addr='서울특별시 중구 퇴계로34길 28'
def index(request):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
    headers = {"Authorization": "KakaoAK 073a393656181c6073880062d3507191"}
    result = json.loads(str(requests.get(url, headers=headers).text))
    match_first = result['documents'][0]['address']
    print(float(match_first['y']), float(match_first['x']))
    return render(request, 'tothers/index.html')

