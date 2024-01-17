import requests

# Создание объекта сессии
session = requests.Session()

# Установка заголовков для сессии
session.headers.update({'User-Agent': 'my_parser'})

# Отправка запроса через объект сессии
response = session.get('https://example.com')

# Доступ к тексту ответа
print(session.headers['User-Agent'])


# Код с сессией

import requests
import time

# Создание объекта сессии
session = requests.Session()

# Измерение времени выполнения запросов с переиспользованием соединения
start_time = time.time()
for _ in range(10):
    response = session.get('https://example.com')
end_time = time.time()

print(f'Время выполнения с переиспользованием соединения: {end_time - start_time}')

# Код без сессии

import requests
import time

# Измерение времени выполнения запросов с переиспользованием соединения
start_time = time.time()
for _ in range(10):
    response = requests.get('https://example.com')
end_time = time.time()

print(f'Время выполнения с переиспользованием соединения: {end_time - start_time}')


#SESSION PROXY
import requests

proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}

session = requests.Session()
session.proxies.update(proxies)

response = session.get('http://example.org')


import requests

url = "https://httpbin.org/ip"
proxies = {
    'http': 'socks5://8ZYk5H:XfMpg7@10.10.36.159:8000',
    'https': 'socks5://Kx4Jcj:h4Ch0N@10.10.51.205:8000',
}

# Создаем сессию
session = requests.Session()

# Устанавливаем прокси для сессии
session.proxies.update(proxies)

# Делаем запрос
response = session.get(url)

print(response.text)