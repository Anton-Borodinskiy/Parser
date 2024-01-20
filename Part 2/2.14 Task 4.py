from bs4 import BeautifulSoup
import requests

request = requests.get(url="https://parsinger.ru/html/index1_page_1.html")
request.encoding = 'utf-8'
soup = BeautifulSoup(request.text, 'html.parser')
p_with_price = soup.find_all("p", attrs={"class":"price"})
total = 0
for p in p_with_price:
    total += int(p.text.split()[0])
print(total)


request = requests.get(url="https://parsinger.ru/html/hdd/4/4_1.html")
request.encoding = 'utf-8'
soup = BeautifulSoup(request.text, 'html.parser')
old = int(soup.find(id="old_price").text.split()[0])
new = int(soup.find(id="price").text.split()[0])
sale = (old - new) * 100 /old
print(round(sale,2))