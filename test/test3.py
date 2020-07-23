import json

# with를 이용해 파일을 연다.
# json 파일은 같은 폴더에 있다고 가정!

with open('example.json',encoding='UTF8') as json_file:
    json_data = json.load(json_file)
    lists = list(json_data)    
print(lists)
#print(json_data)
#for data in json_data:
# print(data)
    
    
