import requests

# Отправляем GET-запрос
r = requests.get('https://api.github.com/events')

# Получаем текст ответа
print("Содержимое ответа:")
print(r.text)
print(r.headers)
# Узнать текущую кодировку
print("Текущая кодировка:", r.encoding)

# Изменить кодировку
r.encoding = 'ISO-8859-1'

# Используйте необходимую кодировку

r.encoding = 'utf-8'

response = requests.get(url='https://jsonplaceholder.typicode.com/todos/')
print(response.json())


# Проверка статуса ответа
if r.status_code == 200:
    print("Запрос успешно выполнен")
else:
    print(f"Произошла ошибка: {r.status_code}")

try:
    r.raise_for_status()
    print("Запрос успешно выполнен")
except requests.exceptions.HTTPError as err:
    print(f"Произошла ошибка: {err}")


response = requests.get(url='http://httpbin.org/image/jpeg')
print(response.content)


# response = requests.get(url='http://httpbin.org/image/jpeg')
# with open('image.jpeg', 'wb') as file: #write byte
#     file.write(response.content)