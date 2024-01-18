from bs4 import BeautifulSoup
# soup.find_all(name, attrs={}, recursive=True, string=None, limit=None, **kwargs)
html = """
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

soup = BeautifulSoup(html, 'html.parser')

# Найти все теги `p`
result = soup.find_all('p')
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с атрибутом class='text-class'
result = soup.find_all('p', attrs={'class': 'text-class'})
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с атрибутом id='text-id'
result = soup.find_all('p', attrs={'id': 'text-id'})
for tag in result:
    print(tag.text)

# Найти все теги `a` с атрибутом href
result = soup.find_all('a', href=True)
for tag in result:
    print(tag['href'], tag.text)


from bs4 import BeautifulSoup

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

# Найти все теги p в HTML-документе, включая те, что находятся внутри вложенных тегов.
all_p_tags = soup.find_all('p', recursive=True)
print(all_p_tags)


soup = BeautifulSoup(html, 'html.parser')

# Найти все теги `p` с текстом 'Текст 1'
result = soup.find_all('p', text='Текст 1')
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с текстом, содержащим 'Текст'
result = soup.find_all('p', text=lambda x: 'Текст' in x)
for tag in result:
    print(tag.text)



# Найти все теги `p` с классом `text-class`
result = soup.find_all('p', {'class': 'text-class'})
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с атрибутом `class`
result = soup.find_all('p', class_=True)
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с атрибутом `id`
result = soup.find_all('p', id=True)
for tag in result:
    print(tag.text)