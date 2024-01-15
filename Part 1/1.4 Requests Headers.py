import requests
import time

# Определение заголовков, которые будут отправлены с запросом
headers = {
    'User-Agent': 'Mozilla/5.0',                  # Идентификация типа браузера, который отправляет запрос
    'Accept': 'text/html,application/xhtml+xml',  # Типы контента, которые клиент может обработать
    'Connection': 'keep-alive'                    # Указание на необходимость использования постоянного соединения
}

# Выполнение GET-запроса с установленными заголовками
response = requests.get('http://httpbin.org/user-agent', headers=headers)

print(response.text)

# Создание словаря с заголовками, которые будут использоваться для маскировки под браузер
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br'
}

# Выполнение GET-запроса с указанными заголовками
response = requests.get('http://httpbin.org/user-agent', headers=headers)

# В переменной response хранится ответ сервера, который можно дальше обработать
print(response.text)
#FAKE USER AGENTS
import requests
from random import choice

url = 'http://httpbin.org/user-agent'

with open('user_agent.txt') as file:
    lines = file.read().split('\n')

for line in lines:
    user_agent = {'user-agent': choice(lines)}
    response = requests.get(url=url, headers=user_agent)
    print(response.text)
    time.sleep(randint(1, 5))
