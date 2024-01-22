import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import csv

url = 'https://parsinger.ru/html/index4_page_1.html'

response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
pages = soup.find(class_="pagen").find_all("a", href=True)

schema = "https://parsinger.ru/html/"
list_to_write = [["Наименование","Бренд", "Форм-фактор", "Ёмкость", "Объем буферной памяти", "Цена"]]
for page in pages:
    url = f'https://parsinger.ru/html/{page["href"]}'
    print(url)
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    all_div = soup.find_all("div", class_="img_box")
    for div in all_div:
        list_for_append = []
        list_for_append.append(div.find("a", class_="name_item").text.strip())
        all_desks = div.find("div", class_="description").text.strip().split("\n")
        for desk in all_desks:
            list_for_append.append(desk.split(":")[-1].strip())
        list_for_append.append(div.find("p", class_="price").text.strip())
        list_to_write.append(list_for_append)
with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    for row in list_to_write:
        writer.writerow(row)
