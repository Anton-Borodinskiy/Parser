#PARENT
from bs4 import BeautifulSoup
import requests

html = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Пример .parent</title>
</head>

<body>
<div id="parent-container">
    <h1 id="main-heading">Заголовок (.parent)</h1>
    <p id="paragraph">Текст абзаца ()</p>

    <ul id="list">
        <li class="list-item">Элемент списка 1</li>
        <li class="list-item">Элемент списка 2</li>
    </ul>
</div>

</body>
</html>

'''

soup = BeautifulSoup(html, "html.parser")
li_elem = soup.find('li', class_='list-item')
parent_elem = li_elem.parent

# Выводим содержимое родительского элемента
print(parent_elem)

print('----разделитель----')

#SIBLING

response = requests.get('https://parsinger.ru/4.1/1/index6.html')
response.encoding = 'utf-8'


soup = BeautifulSoup(response.text, 'html.parser')
# <!-- ... (ваш HTML-код) ... -->
# <div class="section-content">
#     <p class="section-text">Текст раздела 1</p>
#     Дополнительный текст рядом с разделом 1.
# </div>
# <!-- ... (остальной HTML-код) ... -->
# Получаем следующий соседний элемент
sibling = soup.find('p', class_='section-text').next_sibling
print(sibling)

sibling = soup.find(id='section3')
p = sibling.find("p").next_sibling
print(p)

# sibling = soup.find_all('p', class_='section-text')[2].next_sibling

# sibling = soup.find('p', string='Текст раздела 3').next_sibling.text.strip()
#
# tag = soup.find(
#     attrs={
#         'id': 'section3'
#     }
# )
# return tag.div.p.next_sibling
