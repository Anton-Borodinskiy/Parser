from selenium import webdriver
from selenium.webdriver.common.by import By

# Создание объекта ChromeOptions для дополнительных настроек браузера
options_chrome = webdriver.ChromeOptions()

# Добавление аргумента '--headless' для запуска браузера в фоновом режиме
options_chrome.add_argument('--headless')
#Расширение
# options_chrome.add_extension('coordinates.crx')

#Использовать свой профиль
# options_chrome.add_argument('user-data-dir=C:\\Users\\Borod\\AppData\\Local\\Google\\Chrome\\User Data')

# Инициализация драйвера Chrome с указанными опциями
# Использование менеджера контекста 'with' для автоматического закрытия браузера после выполнения кода
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/a/104774'
    browser.get(url)

    # Ищем элемент по тегу 'a' (ссылку)
    a = browser.find_element(By.TAG_NAME, 'a')

    # Выводим атрибут 'href' найденного элемента (URL ссылки)
    print(a.get_attribute('href'))


#EXAMPLE with 2IP
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



url = 'https://2ip.ru/'
with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(5)
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(5)


#PROXY
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

proxy = '8.210.83.33:80'
url = 'https://2ip.ru/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy)

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get(url)
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(5)

#MANY PROXY
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# proxy_list = ['8.210.83.33:80', '199.60.103.28:80',
# '103.151.246.38:10001', '199.60.103.228:80',
# '199.60.103.228:80', '199.60.103.28:80', ]
#
# for PROXY in proxy_list:
#     try:
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('--proxy-server=%s' % PROXY)
#         url = 'https://2ip.ru/'
#
#         with webdriver.Chrome(options=chrome_options) as browser:
#             browser.get(url)
#             print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#
#             browser.set_page_load_timeout(5)
#
#             proxy_list.remove(PROXY)
#     except Exception as _ex:
#         print(f"Превышен timeout ожидания для - {PROXY}")
#         continue

#SOCKS 5 PROXY
# import time
# from selenium.webdriver.common.by import By
# from seleniumwire import webdriver
#
# options = {'proxy': {
#     'http': "socks5://D2Frs6:75JjrW@194.28.210.39:9867",
#     'https': "socks5://D2Frs6:75JjrW@194.28.210.39:9867",
#     }}
#
# url = 'https://2ip.ru/'
#
# with webdriver.Chrome(seleniumwire_options=options) as browser:
#     browser.get(url)
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#     time.sleep(5)