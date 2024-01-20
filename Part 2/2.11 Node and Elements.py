from bs4 import BeautifulSoup
import requests

# Задаем URL-адрес веб-страницы для парсинга
url = 'http://parsinger.ru/html/index1_page_1.html'

# Отправляем GET-запрос к указанной странице
response = requests.get(url=url)

# Устанавливаем кодировку ответа сервера в UTF-8 для корректного отображения текста на кириллице
response.encoding = 'utf-8'

# Преобразуем текст ответа сервера в объект BeautifulSoup с использованием парсера 'lxml'
soup = BeautifulSoup(response.text, 'lxml')

# Ищем на странице первый элемент <div> с классом 'item' и извлекаем из него все вложенные элементы <li>
div = soup.find('div', 'item').find_all('li')
# div = [x.text for x in soup.find('div', 'item').find_all('li')]

# Проходимся по списку найденных элементов <li> и выводим их текстовое содержимое
for txt in div:
    print(txt.text)

print("*"*20)

# Задаем URL-адрес веб-страницы для парсинга
url = 'http://parsinger.ru/html/headphones/5/5_32.html'

# Отправляем GET-запрос к указанной странице
response = requests.get(url=url)

# Устанавливаем кодировку ответа сервера в UTF-8 для корректного отображения текста на кириллице
response.encoding = 'utf-8'

# Преобразуем текст ответа сервера в объект BeautifulSoup с использованием парсера 'lxml'
soup = BeautifulSoup(response.text, 'lxml')

# Ищем на странице тег <p> с классом 'article' и извлекаем из него текстовое содержимое
div = soup.find('p', class_='article').text

# Выводим на экран текст, найденный внутри тега <p> с классом 'article'
print(div)

div = soup.find('p', id='p_header').text

# Выводим на экран текст, найденный внутри тега <p> с идентификатором 'p_header'
print(div)

# Ищем на странице элемент <span> с атрибутом 'name', значение которого равно 'count', и извлекаем его текстовое содержимое
div = soup.find('span', {'name': 'count'}).text

# Выводим на экран извлеченное текстовое содержимое
print(div)