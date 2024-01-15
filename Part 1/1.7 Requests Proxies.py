# Импорт библиотеки для HTTP-запросов
import requests

# Функция для выполнения запроса с использованием прокси
def make_request(url, proxy):
    try:
        response = requests.get(url=url, proxies=proxy)
        print(response.json())
    except Exception as e:
        print(f"Ошибка: {e}")

# URL для тестирования прокси
url = 'http://httpbin.org/ip'

# Прокси для HTTP и HTTPS
proxy_http_https = {
    'http': 'http://103.177.45.3:80',
    'https': 'https://103.177.45.3:80',
}
make_request(url, proxy_http_https)

# Прокси для SOCKS4
proxy_socks4 = {
    'http': 'socks4://103.177.45.3:80',
    'https': 'socks4://103.177.45.3:80',
}
make_request(url, proxy_socks4)

# Прокси для SOCKS5
proxy_socks5 = {
    'http': 'socks5://103.177.45.3:80',
    'https': 'socks5://103.177.45.3:80',
}
make_request(url, proxy_socks5)

# Прокси с авторизацией
proxy_with_auth = {
    'http': 'socks5://login:password@103.177.45.3:80',
    'https': 'socks5://login:password@103.177.45.3:80',
}
make_request(url, proxy_with_auth)

from random import choice
import requests

# Указываем URL, к которому будем отправлять запрос для тестирования прокси
url = 'http://httpbin.org/ip'

# Открываем файл с прокси и читаем его
with open('proxy.txt') as file:
    # Считываем содержимое файла и разделяем его на строки
    proxy_file = file.read().split('\n')

    for _ in range(1000):
        try:
            # Выбираем случайный прокси из списка и удаляем лишние пробелы
            ip = choice(proxy_file).strip()

            # Формируем словарь с прокси для http и https
            proxy = {
                'http': f'http://{ip}',
                'https': f'https://{ip}'
            }
            # Выполняем GET-запрос с использованием выбранного прокси
            response = requests.get(url=url, proxies=proxy)

            # Выводим результат в случае успешного подключения
            print(response.json(), 'Success connection')
        except Exception as _ex:

            # В случае неудачи пропускаем текущую итерацию
            continue
