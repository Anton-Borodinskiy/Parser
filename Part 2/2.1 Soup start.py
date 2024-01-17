from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>Мой сайт</title>
    </head>
    <body>
        <div class="content">
            <p>Привет, мир!</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
title_tag = soup.title
print(title_tag.text)  # Выведет: Мой сайт