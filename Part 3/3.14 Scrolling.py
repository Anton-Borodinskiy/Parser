import time
from selenium import webdriver

with webdriver.Chrome() as browser:
    #СКРОЛЛ ВНИЗ
    browser.get('http://parsinger.ru/scroll/1/')
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    #ВСЯ ВЫСОТА СТРАНИЦЫ
    height = browser.execute_script("return document.body.scrollHeight")
    time.sleep(2)
    print(height)
    #ВИДИМАЯ ЧАСТЬ СТРАНИЦЫ
    height = browser.execute_script("return window.innerHeight")
    time.sleep(2)
    print(height)

with webdriver.Chrome() as browser:
    #СКРОЛЛ НА КОЛ_ВО ПИКСЕЛЕЙ
    browser.get('http://parsinger.ru/scroll/1/')
    for i in range(10):
        browser.execute_script("window.scrollBy(0,5000)")
        time.sleep(2)

