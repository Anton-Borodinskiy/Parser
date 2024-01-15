import requests
from bs4 import BeautifulSoup


# # Отправляем GET-запрос на веб-страницу
# url = 'https://parsinger.ru/2.1/DOM/index2.html'
# response = requests.get(url)
# response.encoding = 'utf-8'
# # Проверяем статус-код ответа
# if response.status_code == 200:
#     # Инициализируем объект BeautifulSoup для парсинга HTML
#     soup = BeautifulSoup(response.text, 'html.parser')
#     target_element = soup.find(id="text777")
#
#     # Извлекаем текст из найденного элемента
#     if target_element:
#         extracted_text = target_element.text
#         print(f"Извлеченный текст: {extracted_text}")  # Вывод на экран
#     else:
#         print("Элемент с ID 'text777' не найден.")
# else:
#     print(f"Не удалось получить доступ к странице, статус-код: {response.status_code}")
#
#
#
# ### HABR !!!!!!!!
# # Отправляем GET-запрос на веб-страницу
# url = 'https://habr.com/ru/articles/top/monthly/'
# response = requests.get(url)
# response.encoding = 'utf-8'
# # Проверяем статус-код ответа
# if response.status_code == 200:
#     # Инициализируем объект BeautifulSoup для парсинга HTML
#     soup = BeautifulSoup(response.text, 'html.parser')
#     target_element = soup.find('a', {'data-test-id': 'article-snippet-title-link'})
#
#     # Извлекаем текст из найденного элемента
#     if target_element:
#         extracted_text = target_element.text
#         print(f"Извлеченный текст: {extracted_text}")  # Вывод на экран
#     else:
#         print("Элемент с ID 'text777' не найден.")
# else:
#     print(f"Не удалось получить доступ к странице, статус-код: {response.status_code}")

# Получаем содержимое веб-страницы
response = requests.get('https://parsinger.ru/2.1/DOM/example.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# Комбинированный поиск: ищем все абзацы с классом "my_class" и атрибутом "data-example"
paragraphs = soup.select('p.my_class[data-example]')

# Выводим найденные элементы
for p in paragraphs:
    print(f'Найденный элемент: {p.text}')