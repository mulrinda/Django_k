from urllib.request import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'g0OhTQflzDelAVixM%2Bm0EtPvJvzcv1ZYwO%2Bj9b%2Fi4bmToDzAyifU%2FHxjCAhbsRMcozdUhj7E9i%2Bc5S7l3JzP9w%3D%3D', quote_plus('ServiceKey') : 'g0OhTQflzDelAVixM%2Bm0EtPvJvzcv1ZYwO%2Bj9b%2Fi4bmToDzAyifU%2FHxjCAhbsRMcozdUhj7E9i%2Bc5S7l3JzP9w%3D%3D', quote_plus('numOfRows') : '10', quote_plus('pageNo') : '1', quote_plus('MobileOS') : 'ETC', quote_plus('MobileApp') : 'AppTest', quote_plus('areaCode') : '1' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)