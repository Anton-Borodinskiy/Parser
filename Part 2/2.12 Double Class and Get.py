from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>Тестовая страница</title>
</head>
<body>
    <div class="class1 class2">Элемент 1</div>
    <div class="class1 class3">Элемент 2</div>
    <div class="class2 class3">Элемент 3</div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

elements = soup.find('div', class_='class1 class2')

# Найдём <div class="class1 class2">Элемент 1</div>
print(elements)

elements = soup.select('div.class1.class2')


# Найдём тот же элемент <div class="class1 class2">Элемент 1</div>
print(elements)


elements = soup.find_all('div', class_=['class1', 'class2'])

# Найдём элементы хотя бы с одним классом

print(elements)

print("*"*20)
# Пример 1: Получение ссылки из тега <a>
html_doc = '<a href="https://example.com">Visit example.com</a>'
soup = BeautifulSoup(html_doc, 'html.parser')

a_tag = soup.find('a')
href_value = a_tag.get('href')

print("Href value:", href_value)  # Вывод: https://example.com
# Пример 3: Попытка получить несуществующий атрибут
html_doc = '<p>Simple paragraph</p>'
soup = BeautifulSoup(html_doc, 'html.parser')

p_tag = soup.find('p')
class_attr = p_tag.get('class')

print("Class attribute:", class_attr)  # Вывод: None

# Пример 2: Извлечение данных из пользовательского атрибута
html_doc = '<div data-info="12345">Some content</div>'
soup = BeautifulSoup(html_doc, 'html.parser')

div_tag = soup.find('div')
data_info = div_tag.get('data-info')

print("Data-info value:", data_info)  # Вывод: 12345