from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index3_page_4.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
category_links = soup.find("div", class_="nav_menu").find_all("a")
schema = "http://parsinger.ru/html/"
all_pages_of_cat = []
for cat in category_links:
    url = f'{schema}{cat["href"]}'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    a_links = soup.find("div", class_="pagen").find_all("a")
    for a in a_links:
        all_pages_of_cat.append(f'{schema}{a["href"]}')
all_pages_of_items = []
for page in all_pages_of_cat:
    response = requests.get(url=page)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    divs = soup.find_all("div", class_="sale_button")
    mouse_links = [f'{schema}{item.find("a")["href"]}' for item in divs]
    all_pages_of_items.extend(mouse_links)
sum_of_all = 0
for item in all_pages_of_items:
    response = requests.get(url=item)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    print(item)
    stock = int(soup.find("span", id="in_stock").text.split()[-1])
    price = int(soup.find("span", id="price").text.split()[0])
    sum_of_all += stock * price
print(sum_of_all)