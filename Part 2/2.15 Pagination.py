from bs4 import BeautifulSoup
import requests

# Задаем URL-адрес веб-страницы для парсинга
url = 'http://parsinger.ru/html/index1_page_3.html'

# Отправляем GET-запрос к указанной странице
response = requests.get(url=url)

# Устанавливаем кодировку ответа сервера в UTF-8 для корректного отображения текста на кириллице
response.encoding = 'utf-8'

# Преобразуем текст ответа сервера в объект BeautifulSoup с использованием парсера 'lxml'
soup = BeautifulSoup(response.text, 'lxml')

# Ищем блок пагинации (элемент <div> с классом 'pagen') на странице,
# затем извлекаем из него все вложенные ссылки (элементы <a>)
pagen = soup.find('div', class_='pagen').find_all('a')

# Выводим на экран список найденных ссылок
print(pagen)

pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
# Выводим на экран список найденных ссылок
print(pagen)

# pagen = []
# for link in soup.find('div', class_='pagen').find_all('a'):
#     pagen.append(link['href'])



# Задаем URL-адрес веб-страницы для парсинга
url = 'http://parsinger.ru/html/index1_page_3.html'

# Отправляем GET-запрос к указанной странице
response = requests.get(url=url)

# Устанавливаем кодировку ответа сервера в UTF-8 для корректного отображения текста на кириллице
response.encoding = 'utf-8'

# Преобразуем текст ответа сервера в объект BeautifulSoup с использованием парсера 'lxml'
soup = BeautifulSoup(response.text, 'lxml')

# Ищем блок пагинации и извлекаем все вложенные ссылки
pagen = soup.find('div', class_='pagen').find_all('a')

# Инициализируем список для хранения абсолютных URL-адресов
list_link = []

# Задаем схему URL-адреса, которая будет использоваться для преобразования относительных путей в абсолютные URL
schema = 'http://parsinger.ru/html/'

# Цикл по всем найденным ссылкам для преобразования их в абсолютные URL-адреса
for link in pagen:
    list_link.append(f"{schema}{link['href']}")

# Выводим на экран список абсолютных URL-адресов
print(list_link)


# from bs4 import BeautifulSoup
# import requests
#
# url = 'http://parsinger.ru/html/index1_page_3.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# schema = 'http://parsinger.ru/html/'
# pagen = [f"{schema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
#
# print(pagen)


from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/index1_page_3.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
schema = 'http://parsinger.ru/html/'
pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]

print(pagen)

# Наглядный псевокод

# from bs4 import BeautifulSoup
# import requests
#
# base_url = "http://сайт.ру/страница_"
# num_page = 1  # начнем с первой страницы
#
# while True:
#     url = f"{base_url}{num_page}"
#     response = requests.get(url)
#
#     # Если статус ответа 200, продолжаем парсинг
#     if ответ.status_code == 200:
#         # Здесь ваш код для парсинга содержимого страницы
#         # ...
#         num_page += 1
#     else:
#         # Если статус ответа не 200, завершаем цикл
#         break