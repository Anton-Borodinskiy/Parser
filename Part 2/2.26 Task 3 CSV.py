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
        list_of_item = []
        list_of_item.append(div.find("a", class_="name_item").text.strip())
        li = div.find_all("li")
        for l in li:
            list_of_item.append(l.text.split(":")[-1].strip())
        list_of_item.append(div.find("p", class_="price").text.strip())
        all_items_cards.append(list_of_item)
with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    for row in all_items_cards:
        writer.writerow(row)
