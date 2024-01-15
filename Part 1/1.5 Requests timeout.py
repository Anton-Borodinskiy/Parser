import requests

try:
    response = requests.get("http://example.com", timeout=.1)
except Exception as e:
    # Узнаем имя возникшего исключения
    print(e.__class__.__name__)


import requests
from requests.exceptions import ConnectTimeout

try:
    response = requests.get("http://example.com", timeout=.1)  # timeout в секундах
except ConnectTimeout:
    print("Connection to the server timed out.")
    # Здесь могут быть дополнительные действия, например, повторный запрос или логирование ошибки.

#Давайте напишем код, чтобы убедиться, что время ожидания запроса через несуществующий прокси-сервер будет действительно значительным.
import requests
import time

url = 'http://httpbin.org/get'

proxies = {
    'http': 'http://200.12.55.90:80',
    'https': 'http://200.12.55.90:80'
}
start = time.perf_counter()
try:
    requests.get(url=url, proxies=proxies, timeout=1)
    # requests.get(url=url, proxies=proxies)
except requests.exceptions.ProxyError as e:
    print(f'wait time = {time.perf_counter() - start}')
    print(e)
except requests.exceptions.ConnectTimeout as e:
    print(f'wait time = {time.perf_counter() - start}')
    print(e)