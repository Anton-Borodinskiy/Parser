import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

url = 'https://parsinger.ru/4.8/6/index.html'

response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

headers = soup.find("thead").find_all("th")
print(headers)
final_list = []
datarows = soup.find("tbody").find_all("tr")
for i in range(len(datarows)):
    price_ok = False
    year_ok = False
    engine_ok = False
    data = datarows[i].find_all("td")
    for k in range(len(data)):
        if headers[k].text == "Стоимость авто" and int(data[k].text) < 4000000:
            price_ok = True
        elif headers[k].text == "Год выпуска" and int(data[k].text) >= 2005:
            year_ok =True
        elif headers[k].text == "Тип двигателя" and data[k].text == "Бензиновый":
            engine_ok = True
    if price_ok and year_ok and engine_ok:
        dict_for_append = {}
        for k in range(len(data)):
            if headers[k].text == "Марка Авто":
                dict_for_append[headers[k].text] = data[k].text
            elif headers[k].text == "Стоимость авто":
                dict_for_append[headers[k].text] = int(data[k].text)
            elif headers[k].text == "Год выпуска":
                dict_for_append[headers[k].text] = int(data[k].text)
            elif headers[k].text == "Тип двигателя":
                dict_for_append[headers[k].text] = data[k].text
        final_list.append(dict_for_append)
sorted_cars = sorted(final_list, key=lambda x: x["Стоимость авто"])
print(json.dumps(sorted_cars, indent=4, ensure_ascii=False))