from bs4 import BeautifulSoup
import requests
import re

request = requests.get("https://parsinger.ru/4.1/1/index4.html")
request.encoding = 'utf-8'

soup = BeautifulSoup(request.text, 'html.parser')
result = soup.find_all('a', attrs={'class': 'name_item product_name'})
for res in result:
    print(res.text.strip())
#     tags = soup.find_all('a', 'name_item')

# tags = soup.find_all('a', class_= 'name_item product_name')

# regex = r'.*_name'
# tags = soup.find_all(attrs={'name': re.compile(regex)})

# tags = soup.select('.name_item.product_name')
# for tag in tags:
#     print(tag.get_text(strip=True))


request = requests.get("https://parsinger.ru/4.1/1/index4.html")
request.encoding = 'utf-8'

soup = BeautifulSoup(request.text, 'html.parser')
result = soup.find_all('p', attrs={'class': 'price product_price'})
count = 0
for res in result:
    count+= int(res.text.replace(" руб","").replace(" ","").strip())

    # res = ''.join([char for char in price.text if char.isdigit()])
    # count += int(res)

    # p1, p2, _ = price.text.split()
    # total += int(f'{p1}{p2}')

print(count)

soup = BeautifulSoup(request.text, 'html.parser')
result = soup.select("li")

# tags_li = soup.find_all('li', id=True)

# [print(j['id']) for j in [i for i in soup.find_all('li')]]

# tags_li = soup.select('li')  # Допишите поиск тегов li
# for tag in tags_li:
#     # Допишите обработку тегов и извлечение идентификаторов
#     tag_id = tag.get('id')
#     if tag_id:
#         print(tag_id)

for li in result:
    print(li["id"])
