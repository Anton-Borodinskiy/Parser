import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import csv

url = 'https://parsinger.ru/html/index2_page_1.html'
all_mobiles = []
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
schema = 'https://parsinger.ru/html/'
all_a = [f'{schema}{x.find("a")["href"]}' for x in soup.find_all('div', class_='sale_button')]
for a in all_a:
    url = a
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    dict_of_mobile = {"categories": "mobile",
                        "name": soup.find("p", id="p_header").text.strip(),
                      "article": soup.find("p", class_="article").text.split(":")[-1].strip(),
                      "description" : {},
                      "count": soup.find("span", id="in_stock").text.split(":")[-1].strip(),
                        "price": soup.find("span", id="price").text.strip(),
                        "old_price": soup.find("span", id="old_price").text.strip(),
                        "link": a

                      }
    all_li = soup.find_all("li")
    for li in all_li:
        dict_of_mobile["description"][li["id"]] = li.text.split(":")[-1].strip()
    all_mobiles.append(dict_of_mobile)
with open('res.json', 'w', encoding='utf-8-sig', newline='') as file:
    json.dump(all_mobiles, file, indent=4, ensure_ascii=False)