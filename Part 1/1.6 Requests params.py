import requests
from bs4 import BeautifulSoup

# Создание словаря с параметрами
params = {'key1': 'value1', 'key2': 'value2'}

# Отправка GET-запроса с параметрами
r = requests.get('https://httpbin.org/get', params=params)

# Вывод результирующего URL
print(r.url)


# Параметры запроса: ищем книги по программированию
params = {'text': 'WEB Парсинг на python'}

# Отправка запроса
response = requests.get('https://yandex.ru/search/', params=params)

# Вывод результатов
print(response.text)

#ПОГОДА
# Ваш API-ключ от OpenWeather (замените на реальный ключ)
api_key = "b6b3b0dbd06ee03102851fc9025c2010"

# Город, для которого мы хотим получить погодные данные
city = "Moscow, RU"

# Словарь параметров для передачи в API
params = {
    'q': city,        # Название города
    'appid': api_key, # Ваш API-ключ
    'units': 'metric' # Единицы измерения (опционально)
}

# Базовый URL API сервиса погоды
base_url = "https://api.openweathermap.org/data/2.5/weather"

# Отправляем GET-запрос к API
response = requests.get(base_url, params=params)
print(response.url)

# Проверяем статус ответа
if response.status_code == 200:
    # Выводим полученные данные о погоде
    print("Погодные данные для города {}: ".format(city))
    print(response.json())
else:
    # Выводим сообщение об ошибке
    print("Не удалось получить данные. Код ошибки: {}".format(response.status_code))
    print(response.text)


# Базовый URL для поиска в онлайн-магазине
base_url = 'https://example.com/search'

# Параметры поиска: ищем ноутбуки с определенными характеристиками
search_params = {
    'query': 'note',  # Поисковый запрос
    'brand': 'Dell',  # Бренд
    'min_price': '50000',  # Минимальная цена
    'max_price': '100000',  # Максимальная цена
    'sort': 'price_asc'  # Сортировка по возрастанию цены
}

# Отправляем GET-запрос с параметрами
response = requests.get(base_url, params=search_params)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсим HTML-страницу с использованием BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все элементы, соответствующие карточкам товаров (здесь это примерный CSS-селектор)
    product_cards = soup.select('.product-card')

    for card in product_cards:
        # Извлекаем информацию из карточки товара (название и цена)
        product_name = card.select_one('.product-name').text
        product_price = card.select_one('.product-price').text

        print(f'Название товара: {product_name}')
        print(f'Цена товара: {product_price}')
        print('---')
else:
    print(f'Не удалось выполнить запрос. Код ошибки: {response.status_code}')
    print(response.url)

import requests
from bs4 import BeautifulSoup

# Базовый URL веб-сайта новостей
base_url = 'https://example.com/news'

# Номер страницы, с которой мы хотим собрать данные
page_number = 2

# Словарь параметров для передачи в запрос
params = {
    'page': page_number  # Параметр для указания номера страницы
}

# Отправляем GET-запрос с параметрами
response = requests.get(base_url, params=params)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсим HTML-страницу с использованием BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все элементы, соответствующие новостным статьям (это примерный CSS-селектор)
    news_articles = soup.select('.news-article')

    for article in news_articles:
        # Извлекаем заголовок каждой статьи
        article_title = article.select_one('.article-title').text
        print(f'Заголовок статьи: {article_title}')
else:
    print(f'Не удалось выполнить запрос. Код ошибки: {response.status_code}')


# Базовый URL для API фильмов
base_url = 'https://api.example.com/movies'

# Параметры для фильтрации фильмов
params = {
    'year_after': 2000,  # Фильмы, выпущенные после этого года
    'genre': 'action'    # Жанр фильма
}

# Отправляем GET-запрос с параметрами для фильтрации
response = requests.get(base_url, params=params)

# Проверка успешности запроса
if response.status_code == 200:
    # Выводим полученные данные о фильмах
    print("Список фильмов:")
    for movie in response.json():
        print(f'  Название: {movie["title"]}, Год выпуска: {movie["year"]}, Жанр: {movie["genre"]}')
else:
    # Выводим сообщение об ошибке
    print(f'Не удалось выполнить запрос. Код ошибки: {response.status_code}')