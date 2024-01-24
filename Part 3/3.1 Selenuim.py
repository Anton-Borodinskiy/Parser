
# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType
# from selenium.webdriver.chrome.service import Service as ChromiumService
#
# with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as driver:
#     driver.get("https://stepik.org/course/104774")
#     time.sleep(5)
#
#
# import time
# from selenium import webdriver
#
# with webdriver.Chrome() as driver:
#     driver.get("https://stepik.org/a/104774")
#     time.sleep(5)

#COORDINATES
import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('coordinates.crx')


with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/course/104774'
    browser.get(url)
    time.sleep(15)



# # Создание объекта ChromeOptions
# options = webdriver.ChromeOptions()

# # Добавление аргументов командной строки
# options.add_argument('--headless')  # Запуск браузера в фоновом режиме (без GUI)
# options.add_argument('--disable-gpu')  # Отключение GPU (полезно для старых версий Chrome)
# options.add_argument('--no-sandbox')  # Отключение режима "песочницы" (sandbox)

# # Запуск экземпляра браузера Chrome с заданными опциями
# driver = webdriver.Chrome(options=options)