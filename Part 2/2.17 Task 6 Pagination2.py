from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index3_page_4.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
a_links = soup.find("div", class_="pagen").find_all("a")
schema = "http://parsinger.ru/html/"
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
sum_of_all = 0
for link in urls_of_mice:
    response = requests.get(url=link)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    sum_of_all += int(soup.find("p", class_="article").text.split()[-1])
print(sum_of_all)