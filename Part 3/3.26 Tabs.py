# .current_window_handle — возвращает дескриптор текущей вкладки;
# .window_handles — возвращает список всех дескрипторов открытых вкладок;
# .switch_to.window(window_handles[0]) — переключает фокус между вкладками.


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
#TASK2
sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]
with webdriver.Chrome() as browser:
    digits = []
    for i in range(len(sites)):
        browser.execute_script(f'window.open("{sites[i]}", "_blank{i}");')
    tabs = browser.window_handles
    for tab in range(len(tabs)):
        try:
            browser.switch_to.window(browser.window_handles[tab])
            browser.find_element(By.CLASS_NAME, "checkbox_class").click()
            time.sleep(0.3)
            digits.append(int(browser.find_element(By.ID, "result").text))
        except:
            pass
    for i in range(len(digits)):
        digits[i] = math.sqrt(digits[i])

    print(round(sum(digits),9))

#EXAMPLE
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# result = []
# with webdriver.Chrome() as browser:
#     for x in range(1, 7):
#         blank = browser.execute_script(f'window.open("http://parsinger.ru/blank/1/{x}.html", "_blank{x}");')
#     tabs = browser.window_handles
#     for z in range(len(tabs) - 1):
#         if not browser.execute_script("return document.title;"):
#             browser.close()
#         browser.switch_to.window(browser.window_handles[z])
#         browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
#         result.append(math.sqrt(int(browser.find_element(By.ID, 'result').text)))
#
# print(sum(result))


#TASK1
# with webdriver.Chrome() as browser:
#     count = 0
#     browser.get('http://parsinger.ru/blank/3/index.html')
#     [x.click() for x in browser.find_elements(By.CLASS_NAME, 'buttons')]
#     tabs = browser.window_handles
#     for tab in range(len(tabs)):
#         browser.switch_to.window(browser.window_handles[tab])
#         title = browser.execute_script("return document.title;")
#         if title.isdigit():
#             count += int(title)
#     print(count)

with webdriver.Chrome() as browser:
    sum_of_all = 0
    browser.get('https://parsinger.ru/blank/3/index.html')
    buttons = len(browser.find_elements(By.CLASS_NAME, "buttons"))
    for i in range(buttons):
        browser.execute_script(f'window.open("https://parsinger.ru/blank/3/{i+1}.html", "_blank{i+2}");')
        time.sleep(1)
    for x in range(len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[x])
        time.sleep(1)
        if browser.execute_script("return document.title;").isdigit():
            sum_of_all += int(browser.execute_script("return document.title;"))
    print(sum_of_all)
#THEORY
with webdriver.Chrome() as browser:
    time.sleep(1)
    browser.execute_script('window.open("http://parsinger.ru/blank/0/1.html", "_blank1");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/2.html", "_blank2");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/3.html", "_blank3");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/4.html", "_blank4");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/5.html", "_blank5");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/6.html", "_blank6");')

    for x in range(len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[x])
        time.sleep(1)
        print(browser.execute_script("return document.title;"), browser.window_handles[x])

with webdriver.Chrome() as browser:
    #browser.get("https://stepik.org/course/104774/promo") # Вместо вкладки data; будет вкладка в которой будет загружен степик
    browser.execute_script('window.open("http://parsinger.ru/blank/2/1.html", "_blank1");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank2");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank3");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank4");')

    for x in range(len(browser.window_handles)):  #reversed(range(len(browser.window_handles))) Для итерирования по порядку
        browser.switch_to.window(browser.window_handles[x])
        for y in browser.find_elements(By.CLASS_NAME, 'check'):
            y.click()

with webdriver.Chrome() as browser:
    result = []
    browser.get('http://parsinger.ru/blank/2/1.html')
    time.sleep(1)
    browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank1");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank2");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank3");')
    time.sleep(2)
    print(browser.window_handles)
