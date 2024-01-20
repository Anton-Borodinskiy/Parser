from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
a_links = soup.find("div", class_="pagen").find_all("a")
schema = "http://parsinger.ru/html/"
urls_to_parse = []
for a in a_links:
    urls_to_parse.append(f'{schema}{a["href"]}')
full_list = []
for link in urls_to_parse:
    response = requests.get(url=link)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    names = [item.text for item in soup.find_all("a", class_="name_item")]
    full_list.append(names)
print(full_list)
