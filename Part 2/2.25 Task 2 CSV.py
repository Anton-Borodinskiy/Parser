from bs4 import BeautifulSoup
import requests
import csv

url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
a_links = soup.find("div", class_="pagen").find_all("a")
schema = "https://parsinger.ru/html/"
urls_to_parse = []
for a in a_links:
    urls_to_parse.append(f'{schema}{a["href"]}')
urls_of_mice = []

full_list = []
for link in urls_to_parse:
    response = requests.get(url=link)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    divs = soup.find_all("div", class_="sale_button")
    mouse_links = [f'{schema}{item.find("a")["href"]}' for item in divs]
    urls_of_mice.extend(mouse_links)
print(urls_of_mice)
list_to_write = [["Наименование","Артикул","Бренд","Модель","Тип","Технология экрана","Материал корпуса","Материал браслета","Размер","Сайт производителя","Наличие","Цена","Старая цена","Ссылка на карточку с товаром"]]
for link in urls_of_mice:
    response = requests.get(url=link)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    list_for_append = []
    list_for_append.append(soup.find("p", id="p_header").text)
    list_for_append.append(soup.find("p", class_="article").text.split(":")[-1].strip())
    list_for_append.append(soup.find("li", id="brand").text.split(":")[-1].strip())
    list_for_append.append(soup.find("li", id="model").text.split(":")[-1].strip())
    list_for_append.append(soup.find("li", id="type").text.split(":")[-1].strip())
    list_for_append.append(soup.find("li", id="display").text.split(":")[-1].strip())
    list_for_append.append(soup.find("li", id="material_frame").text.split(":")[-1].strip())
    list_for_append.append(soup.find("li", id="material_bracer").text.split(":")[-1].strip())
    list_for_append.append(soup.find("li", id="size").text.split(":")[-1].strip())
    list_for_append.append(soup.find("li", id="site").text.split(":")[-1].strip())
    list_for_append.append(soup.find("span", id="in_stock").text.split(":")[-1].strip())
    list_for_append.append(soup.find("span", id="price").text)
    list_for_append.append(soup.find("span", id="old_price").text)
    list_for_append.append(link)
    list_to_write.append(list_for_append)
with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    for row in list_to_write:
        writer.writerow(row)

