try:
    response = requests.get('https://example.com')
except Exception as e:
    print(f"Произошла ошибка: {e}")

import requests
try:
    response = requests.get('https://example322.com')
except requests.ConnectionError as e:
    print(f"Произошла ошибка соединения: {e}")

try:
    response = requests.get('https://nonexistentwebsite123456.com')
except requests.RequestException as e:
    print('Произошла ошибка: ', str(e)) #ALL EXCEPTIONS OF LIBRARY


try:
    response = requests.get('https://httpstat.us/500')
    response.raise_for_status()
except requests.HTTPError as e:
    print('HTTP ошибка: ', str(e))

try:
    response = requests.get('')
except requests.exceptions.MissingSchema as e:
    print('Требуется URL с указанием схемы: ', str(e))

try:
    response = requests.get('http://httpbin.org/relative-redirect/32', allow_redirects=True,)
except requests.TooManyRedirects as e:
    print('Слишком много перенаправлений: ', str(e))

try:
    response = requests.get('https://httpstat.us/200', timeout=0.001)
except requests.ConnectTimeout as e:
    print('Тайм-аут соединения: ', str(e))

try:
    response = requests.get('https://httpstat.us/200?sleep=5000', timeout=1)
except requests.ReadTimeout as e:
    print('Тайм-аут чтения: ', str(e))

import requests

try:
    response = requests.get('https://httpstat.us/200?sleep=5000', timeout=1)
except requests.Timeout as e:
    print('Тайм-аут запроса: ', str(e)) #ALL TIMEOUTS


import requests

try:
    response = requests.get('https://httpstat.us/200')
    data = response.json()
except requests.JSONDecodeError as e:
    print('Ошибка декодирования JSON: ', str(e))