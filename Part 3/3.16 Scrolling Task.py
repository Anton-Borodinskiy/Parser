import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

#TASK3



#TASK2
with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/selenium/5.7/1/index.html')
    all_btn = webdriver.find_elements(By.TAG_NAME,"button")
    for btn in all_btn:
        webdriver.execute_script("return arguments[0].scrollIntoView(true);", btn)
        btn.click()
    # webdriver.switch_to.frame("frame_name") - Переключает фокус на указанный фрейм.
    alert = webdriver.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    time.sleep(20)
#EXAMPLE1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# driver = webdriver.Chrome()  # или любой другой драйвер, который у вас установлен
# driver.get('https://parsinger.ru/selenium/5.7/1/index.html')  # замените на URL вашего сайта
#
# # Находим все кнопки на странице
# buttons = driver.find_elements(By.CLASS_NAME, "clickMe")
# time.sleep(1)
#
# count = 0
# for button in buttons:
#     # Прокрутка до кнопки
#     driver.execute_script("return arguments[0].scrollIntoView(true);", button)
#     # time.sleep(.2)  # Пауза для уверенности, что страница прокрутилась и элемент видим
#     button.click()  # Нажимаем на кнопку
#     count += 1
#
#
# wait = WebDriverWait(driver, 10)
# alert = wait.until(EC.alert_is_present())
# alert_text = alert.text
# alert.accept()
#
# print(alert_text)
# print(count)

#EXAMPLE2
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
#     while True:
#         if browser.execute_script("return document.readyState;") == 'complete':
#             break
#
#     for button in browser.find_elements(By.CLASS_NAME, 'clickMe'):
#         browser.execute_script('return arguments[0].scrollIntoView(true);', button)
#         button.click()
#
#     alert = browser.switch_to.alert.text
#     print(alert)

#TASK1
with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/scroll/4/index.html')
    all_btn = webdriver.find_elements(By.TAG_NAME,"button")
    sum_all = 0
    for btn in all_btn:
        webdriver.execute_script("return arguments[0].scrollIntoView(true);", btn)
        btn.click()
        sum_all += int(webdriver.find_element(By.ID,"result").text)
    print(sum_all)

