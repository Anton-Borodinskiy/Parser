from bs4 import BeautifulSoup

# Пример HTML-строки
html_string = """
<div>
    <p>Первый абзац.</p>
    <p>Второй абзац <span>со вложенным</span> текстом.</p>
</div>
"""

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html_string, 'html.parser')

# Использование .text для извлечения всего текста из div
div_text = soup.find('div').text

print(div_text)

# Тот же пример HTML-строки
html_string = """
<div>
    <p>Первый абзац.</p>
    <p>Второй абзац <span>со вложенным</span> текстом.</p>
</div>
"""

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html_string, 'html.parser')

# Использование .get_text() с параметром separator
div_text = soup.find('div').get_text(separator=" | ")

print(div_text)


# soup.find(name, attrs={}, recursive=True, string, **kwargs)

# Здесь 'tag' - это имя тега, а 'your_id' - значение атрибута id.

soup.find('tag', id='your_id')

# Заметьте, что используется class_ вместо class, так как class является зарезервированным словом в Python.

soup.find('tag', class_='your_class')

# Здесь 'data-attribute' - это имя пользовательского атрибута, а 'value' - его значение.

soup.find('tag', {'data-attribute': 'value'})

# Здесь у тега одновременно должны быть два атрибута с заданными значениями.

soup.find('tag', {'data-attribute1': 'value1', 'data-attribute2': 'value2'})

# Указываются оба класса, разделенные пробелом.

soup.find('tag', class_='class1 class2')

# Если класс формируется динамически и вы знаете только часть названия, можно использовать регулярные выражения:

import re
soup.find('tag', class_=re.compile('your_dynamic_part'))

# 'your_dynamic_part' - часть имени класса.

soup.find('tag', {'data-attribute': re.compile('dynamic_part')})

# Просто укажите имя тега:
# Это найдет первый тег с указанным именем без учета его атрибутов.

soup.find('tag')



html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <h1>Hello World</h1>
        <p class="info">This is a paragraph.</p>
        <p class="info">This is another paragraph.</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Найдёт первый тег h1
first_h1 = soup.find('h1')
print(first_h1)

print('----разделитель----')

# Найдёт первый тег p с классом "info"
first_p = soup.find('p', {'class': 'info'})
print(first_p)


html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <div id="main">
            <h1>Hello World</h1>
            <p class="info">This is a paragraph.</p>
            <p class="info">This is another paragraph.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
        <div id="secondary">
            <p>Some additional information.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Находим первый div с id "main"
main_div = soup.find('div', {'id': 'main'})
print(main_div)

print('----разделитель----')

# Найдите первый тег h1 внутри «основного» div
main_h1 = main_div.find('h1')
print(main_h1)

print('----разделитель----')

# Найдите первый тег p с классом «информация» внутри «основного» div
main_p = main_div.find('p', {'class': 'info'})
print(main_p)

print('----разделитель----')

# Найдите первый тег ul внутри «основного» div
main_ul = main_div.find('ul')
print(main_ul)



html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <div id="main">
            <h1>Hello World</h1>
            <p class="info">This is a paragraph.</p>
            <p class="info">This is another paragraph.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
        <div id="secondary">
            <p>Some additional information.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Найдите первый div с идентификатором «main»
main_div = soup.find('div', attrs={'id': 'main'})
print(main_div)

print('----разделитель----')

# Найдите первый тег p с классом "info"
info_p = soup.find('p', attrs={'class': 'info'})
print(info_p)




def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    li_tag = soup.find("li", {"class": ["description", "detailz"]})
    li_tag = soup.find(class_='description detailz').text
    li_tag = soup.find('li', class_='description detailz').text



tag = soup.find('div', {
    'class': ["description_detail", 'class1', 'class2', 'class3'],
    'data-fdg45': 'value_user',
    'data-54dfg60': 'value_key',
    'data-d6f50hg': 'value_value'
})

tag = soup.find(attrs = {
    'class': ["description_detail", 'class1', 'class2', 'class3'],
    'data-fdg45': 'value13',
    'data-54dfg60': 'value14',
    'data-d6f50hg': 'value15'
})# Допишите поиск тега в супе и извлеките текст