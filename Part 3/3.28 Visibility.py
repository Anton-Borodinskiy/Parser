# EC.presence_of_element_located(locator)— Это одно из ожидаемых условий , которое помогает нам убедиться, что элемент присутствует на веб-странице.
# EC.visibility_of_element_located(locator)— Это одно из ожидаемых условий, позволяющее убедиться, что элемент не только присутствует на странице, но и видим пользователю.
# EC.visibility_of(element)— Это условие ожидания, которое проверяет, является ли конкретный элемент видимым на веб-странице.
# EC.presence_of_all_elements_located(locators)— В некоторых ситуациях вам может потребоваться работать не с одним элементом, а с группой элементов, например, со списком или рядом кнопок. Используя это условие, вы можете удостовериться, что все эти элементы загрузились и присутствуют на странице перед тем, как начать с ними взаимодействие. Метод проверяет наличие всех элементов, указанных локатором, в DOM-структуре страницы. Однако стоит помнить, что "присутствие" не гарантирует "видимость" элемента.
# EC.visibility_of_any_elements_located(locator)— Это ожидаемое условие, которое проверяет видимость хотя бы одного элемента из группы элементов, соответствующих заданному локатору.
# EC.visibility_of_all_elements_located(locator)— Это ожидаемое условие, которое убеждается в том, что абсолютно все элементы, соответствующие указанному локатору, являются видимыми на веб-странице.

# WebDriverWait(browser, poll_frequency=0.5, timeout=10).until(EC.presence_of_element_located(locator))

# EC.presence_of_element_located(locator)— Это одно из ожидаемых условий , которое помогает нам убедиться, что элемент присутствует на веб-странице.
#
# locator— кортеж, содержащий два элемента: тип поиска (By.ID, By.XPATH и т. д.) и значение для поиска.


# locator = (By.ID, 'some_element_id')
# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))


# locator = (By.XPATH, '//div[@class="visible_class"]')
# element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))

# element = driver.find_element(By.ID, 'visible_element_id')
# visible_element = WebDriverWait(driver, 10).until(EC.visibility_of(element))


# locator = (By.CLASS_NAME, 'some_class_name')
# elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(locator))

# locator = (By.TAG_NAME, 'li')
# visible_elements = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located(locator))

# locator = (By.CSS_SELECTOR, '.visible_elements')
# all_visible_elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(locator))

import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#TASK3
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/3/index.html')
    ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
                   'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']
    locator = (By.ID, ids_to_find)
    clicked = []
    while True:
        elements = WebDriverWait(browser, 100).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[contains(@class, "box")]')))
        for element in elements:
            elem_id = element.get_attribute("id")
            if elem_id in ids_to_find:
                element.click()
#EXAMPLE
# # Инициализация драйвера
# driver = webdriver.Chrome()
#
# # Открываем указанную страницу
# driver.get("https://parsinger.ru/selenium/5.9/3/index.html")
#
# # Список ID, которые мы ищем
# ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
#                'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']
#
# for id in ids_to_find:
#     # Получаем элемент без ожидания
#     element = driver.find_element(By.ID, id)
#
#     # Теперь ожидаем, пока элемент станет видимым
#     WebDriverWait(driver, 100).until(EC.visibility_of(element))
#
#     # Кликаем по элементу
#     element.click()
#
# # Ожидаем появление алерта
# alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
# # Получаем текст из алерта
# alert_text = alert.text
# # Закрываем алерт
# alert.accept()
#
# print(alert_text)
#
# # Закрываем браузер
# driver.quit()

#TASK2
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/2/index.html')
    locator = (By.ID, "qQm9y1rk")
    WebDriverWait(browser, 40).until(EC.visibility_of_element_located(locator)).click()
    time.sleep(10)
    alert = browser.switch_to.alert # Если вы планируете что-то делать с этим событием, можно добавить его в переменную
    print(alert.text)

# EXAMPLE
# # Создаем драйвер браузера (например, Chrome)
# driver = webdriver.Chrome()
#
# # Открываем страницу
# driver.get("https://parsinger.ru/selenium/5.9/2/index.html")
#
# seen_ids = set()  # Множество для хранения уже увиденных ID
#
# try:
#     while True:
#         try:
#             # Ожидаем появления всех элементов класса "box" внутри main_container
#             elements = WebDriverWait(driver, 100).until(
#                 EC.presence_of_all_elements_located((By.XPATH, '//*[@id="main_container"]//*[contains(@class, "box")]'))
#             )
#
#             for element in elements:
#                 elem_id = element.get_attribute("id")
#                 if elem_id not in seen_ids:
#                     print(f"New element found with ID: {elem_id}")
#                     seen_ids.add(elem_id)
#
#                     if elem_id == "qQm9y1rk":
#                         element.click()
#                         alert = driver.switch_to.alert
#                         alert_text = alert.text
#                         alert.accept()
#                         print(f"Alert text: {alert_text}")
#
#         except StaleElementReferenceException:
#             # Если возникла ошибка из-за устаревшего элемента, просто повторяем цикл
#             continue
#
# except KeyboardInterrupt:
#     # Это позволит вам прервать выполнение кода при необходимости
#     pass
#
# finally:
#     # Закрываем драйвер
#     driver.quit()

#TASK1
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/6/index.html')
    locator = (By.CLASS_NAME, "BMH21YY")
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located(locator))
    print(browser.find_element(By.CLASS_NAME, "BMH21YY").text)

#EXAMPLE
# url = 'http://parsinger.ru/expectations/5/index.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
#     elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'BMH21YY')))
#     print(elem.text)