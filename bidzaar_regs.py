import bs4
import requests
import json

#file register

cookies = {
  'your_coolkies_from_site',
}

headers = {
    'your_headers_from_site',
}

params = {
    'paging.page': '1',
    'paging.size': '1',
    'sorting.key': 'publishDate',
    'sorting.direction': 'desc',
    'logic': 'and',
    'filters[0].operator': 'in',
    'filters[0].field': 'status',
    'filters[0].value': '[1]',
    'filters[1].operator': 'eq',
    'filters[1].field': 'procedureType',
    'filters[1].value': '3',
}

response = requests.get(
    'https://bidzaar.com/api/process/light/procedures/available',
    params=params,
    cookies=cookies,
    headers=headers,
)

html = response.content
#soup = BeautifulSoup(html, 'lxml')
html = json.loads(html)
#print(html)

total = html["totalCount"]
print("идёт парсинг "+ str(total)+" реестров сайта https://bidzaar.com:")

cookies = {
  'your_coolkies_from_site',
}

headers = {
    'your_headers_from_site',
}

params = {
    'paging.page': '1',
    'paging.size': str(total),
    'sorting.key': 'publishDate',
    'sorting.direction': 'desc',
    'logic': 'and',
    'filters[0].operator': 'in',
    'filters[0].field': 'status',
    'filters[0].value': '[1]',
    'filters[1].operator': 'eq',
    'filters[1].field': 'procedureType',
    'filters[1].value': '3',
}

response = requests.get(
    'https://bidzaar.com/api/process/light/procedures/available',
    params=params,
    cookies=cookies,
    headers=headers,
)
html = response.content
#soup = BeautifulSoup(html, 'lxml')
html = json.loads(html)
names = input("Введите ключевое слово: ")
fr = 0
for data in html["items"]:
    link = 'https://bidzaar.com/process/light/'+str(data["id"])+'/request'
    number = data["number"]
    name = data["name"]
    if names in name.strip():
        fr+=1
        print(str(fr)+" номер: "+str(number)+ " - " +name+ " - " +link)
if fr == 0:
    print("по запросу "+str(names) +" нечего не анйдено")
