#EXAMPLES
import requests
# Указываем параметры запроса в виде словаря
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://www.example.com', params=params)
from requests.auth import HTTPBasicAuth

# Указываем логин и пароль
response = requests.get('https://www.example.com', auth=HTTPBasicAuth('user', 'pass'))

# Создаем сессию
with requests.Session() as s:
    s.get('https://www.example.com/login')
    response = s.get('https://www.example.com/data')

try:
    response = requests.get('https://www.example.com', timeout=1)
except requests.Timeout:
    print("Слишком долгое ожидание!")
except requests.RequestException as e:
    print(f"Произошла ошибка: {e}")


# Открываем файл и отправляем его на сервер
with open('file.txt', 'rb') as f:
    files = {'file': f}
    response = requests.post('https://www.example.com/upload', files=files)

# Загрузка файла с сервера по частям
with requests.get('https://www.example.com/file', stream=True) as r:
    with open('file.txt', 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

# Отправляем данные в формате словаря dict

data = {'name': 'John', 'age': 30}
response = requests.post('https://www.example.com/api', json=data)

# Использование куки в сессии
with requests.Session() as s:
    s.get('https://www.example.com/login')
    cookies = dict(cookies_are='working')
    response = s.get('https://www.example.com/data', cookies=cookies)


# Автоматическое следование редиректам
response = requests.get('https://www.example.com/redirect', allow_redirects=True)