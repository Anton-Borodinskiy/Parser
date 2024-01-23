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
list_to_write = []
    # [["Наименование","Бренд", "Форм-фактор", "Ёмкость", "Объем буферной памяти", "Цена"]]
for page in pages:
    url = f'https://parsinger.ru/html/{page["href"]}'
    print(url)
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    all_div = soup.find_all("div", class_="img_box")
    for div in all_div:
        dict_for_append = {}
        dict_for_append["Наименование"] = div.find("a", class_="name_item").text.strip()
        all_desks = div.find("div", class_="description").text.strip().split("\n")
        for desk in all_desks:
            dict_for_append[desk.split(":")[0].strip()] = desk.split(":")[-1].strip()
        dict_for_append["Цена"] = div.find("p", class_="price").text.strip()
        list_to_write.append(dict_for_append)
print(list_to_write)
# with open('res.json', 'w', encoding='utf-8-sig', newline='') as file:
#     json.dump(list_to_write, file, indent=4, ensure_ascii=False)



from bs4 import BeautifulSoup
import requests
import csv
url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
category_links = soup.find("div", class_="nav_menu").find_all("a")
schema = "https://parsinger.ru/html/"
all_pages_of_cat = []
for cat in category_links:
    url = f'{schema}{cat["href"]}'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    a_links = soup.find("div", class_="pagen").find_all("a")
    for a in a_links:
        all_pages_of_cat.append(f'{schema}{a["href"]}')
all_items_cards = []
for page in all_pages_of_cat:
    url = page
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    all_divs = soup.find_all("div", class_="img_box")
    for div in all_divs:
        dict_of_item = {}
        dict_of_item["Наименование"] = div.find("a", class_="name_item").text.strip()
        li = div.find_all("li")
        for l in li:
            dict_of_item[l.text.split(":")[0].strip()] = l.text.split(":")[-1].strip()
        dict_of_item["Цена"] = div.find("p", class_="price").text.strip()
        all_items_cards.append(dict_of_item)

with open('res.json', 'w', encoding='utf-8-sig', newline='') as file:
    json.dump(all_items_cards, file, indent=4, ensure_ascii=False)