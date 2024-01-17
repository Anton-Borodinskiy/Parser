from bs4 import BeautifulSoup
import requests
import lxml

# Пример 1. Передача файла HTML напрямую без использования менеджера контекста
file = open('index.html', encoding='utf-8')
soup = BeautifulSoup(file, 'lxml')
file.close()
print("Анализ файла без использования менеджера контекста:\n", soup)

# Пример 2. Передача файла HTML с использованием менеджера контекста
with open('index.html', 'r', encoding='utf-8') as file:
    soup2 = BeautifulSoup(file, 'lxml')
    print("Анализ файла с использованием менеджера контекста:\n", soup2)
# Пример 3. Передача объекта response прямо из запроса
response = requests.get(url='http://parsinger.ru/html/watch/1/1_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

print(soup)

html = "<div class='myclass'>Hello, world!</div> <h1 class='notmyclass'>Hello, world!</h1>"
soup = BeautifulSoup(html, 'html.parser')

tag = soup.div

print(type(tag))   # <class 'bs4.element.Tag'>
print(tag.name)    # div
print(tag.attrs)   # {'class': ['myclass']}
print(tag.string)  # Hello, world!