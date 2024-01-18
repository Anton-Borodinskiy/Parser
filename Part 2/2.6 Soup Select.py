from bs4 import BeautifulSoup
# soup.select(selector, namespaces=None, limit=None, **kwargs)
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
            <p class="info">This is another .</p>
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
# Элементы, содержащие определенный текст
soup = BeautifulSoup(html, 'html.parser')
elements = soup.select("p")
elements_with_text = [elem for elem in elements if "paragraph" in elem.text]
for elem in elements_with_text:
    print(elem.text)


# Тег: select("p")
# Класс: select(".class")
# Идентификатор: select("#id")
# Атрибут: select("[attribute=value]")
# Несколько селекторов: select("p.class")
# Вложенные элементы: select("div span")
# Непосредственные дочерние элементы: select("div > p")
# Элементы с несколькими классами: select(".class1.class2")
# Элементы с определенными атрибутами: select("[data-custom]")
# Псевдоклассы CSS: select("p:first-of-type") или select("p:last-of-type")
# Соседние элементы: select("h1 + p")


html = """
<html>
    <body>
        <h1>Заголовок 1</h1>
        <p class="text-class">Текст 1</p>
        <p class="text-class">Текст 2</p>
        <p id="text-id">Текст 3</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Найти все теги `p` с классом `text-class`
result = soup.select('p.text-class')
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с атрибутом `id`
result = soup.select('p#text-id')
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` внутри тега `body`
result = soup.select('body p')
for tag in result:
    print(tag.text)


html = """
<html>
  <body>
    <p class="highlight">This is a highlighted paragraph.</p>
    <p>This is a normal paragraph.</p>
    <div id="div1">
      <p>This is a paragraph in a div.</p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Выберем все параграфы с классом "highlight"
highlighted_paras = soup.select(".highlight")
for para in highlighted_paras:
    print(para.text)

print('----разделитель----')

# Выберем все параграфы, находящиеся внутри элемента с идентификатором "div1"
div_paras = soup.select("#div1 p")
for para in div_paras:
    print(para.text)



html = """
<html>
  <body>
    <div id="div1">
      <p class="highlight">This is a highlighted paragraph in div1.</p>
      <p>This is a normal paragraph in div1.</p>
    </div>
    <div id="div2">
      <p class="highlight">This is a highlighted paragraph in div2.</p>
      <p>This is a normal paragraph in div2.</p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Выберем все параграфы с классом "highlight", которые
# находятся внутри элементов с идентификатором "div1" или "div2"
highlighted_paras = soup.select("#div1 .highlight, #div2 .highlight")
print("Highlighted paragraphs:")
for para in highlighted_paras:
    print(para.text)
print('----разделитель----')
soup = BeautifulSoup(html, "html.parser")

# Выберем все параграфы с классом "highlight"
highlighted_paras = soup.select("p[class='highlight']")
print("Highlighted paragraphs:")
for para in highlighted_paras:
    print(para.text)