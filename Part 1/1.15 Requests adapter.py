# Создание адаптера с пользовательской конфигурацией


import requests
from requests.adapters import HTTPAdapter

# Создаем сессию
session = requests.Session()

# Создаем адаптер с конфигурацией по умолчанию
adapter = HTTPAdapter(
    pool_connections=10,         # Количество соединений в пуле
    pool_maxsize=20,             # Максимальное количество соединений в пуле
    max_retries=5,               # Стратегия повторных попыток
    pool_block=True              # Блокировать или нет, когда пул соединений полон
)


# Монтируем адаптер для HTTP и HTTPS
session.mount('http://', adapter)
session.mount('https://', adapter)

# Теперь можно делать запросы через эту сессию
response = session.get('https://httpbin.org/get')
print(response.status_code)  # 200


#BIG EXAMPLE
import requests
from requests.adapters import HTTPAdapter

# Список прокси
proxies_list = [
    {"http": "http://10.10.1.11:3128", "https": "socks5://10.10.10.11:3128"},
    {"http": "socks5://10.10.10.159:8000", "https": "socks5://10.10.10.159:8000"},
        #...
    {"http": "socks5://10.10.10.216:8000", "https": "socks5://10.10.10.216:8000"},
]
# Создание сессии
session = requests.Session()

def make_request(proxy):
    adapter = HTTPAdapter()
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    try:
        response = session.get('https://httpbin.org/get', proxies=proxy, timeout=5)
        print(f'Успех с прокси {proxy}: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Не удалось использовать прокси {proxy}: {str(e)}')
        return False   # Возврат False при неудачной попытке
    return True        # Возврат True при успешной попытке

# Перебор прокси и запросов
proxy_index = 0
for i in range(5):
    success = make_request(proxies_list[proxy_index])
    if not success:
        proxy_index = (proxy_index + 1) % len(proxies_list)       # Переход к следующему прокси
        success = make_request(proxies_list[proxy_index])         # Повторный запрос с новым прокси

# Закрытие сессии
session.close()