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

from bs4 import BeautifulSoup

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

# Выберем первый параграф с классом "highlight"
highlighted_para = soup.select_one("p[class='highlight']")
print("Highlighted paragraph:")
print(highlighted_para.text)
print('----разделитель----')
html_doc = """
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <div class="container">
            <p>This is a paragraph.</p>
            <p>This is another paragraph.</p>
        </div>
        <div class="container">
            <p class="highlight">This is a highlighted paragraph.</p>
            <p>This is a fourth paragraph.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Выберем первый div с классом "container"
first_container = soup.select_one('.container')
print(first_container)
print('----разделитель----')
soup = BeautifulSoup(html_doc, 'html.parser')

# Выберем первый div с классом «container», у которого есть дочерний элемент p с классом «highlight».
highlighted_paragraph = soup.select_one('.container p.highlight')
print(highlighted_paragraph)
print('----разделитель----')
