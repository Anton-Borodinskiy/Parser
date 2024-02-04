import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#TASK4
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/7/index.html')
    checkbox = browser.find_elements(By.TAG_NAME, "input")
    buttons = browser.find_elements(By.XPATH, "//div[@class='container']/button")
    for i in range(len(checkbox)):
        WebDriverWait(browser, 100).until(EC.element_to_be_selected(checkbox[i]))
        buttons[i].click()
    print(browser.find_element(By.TAG_NAME, "p").text)
#EXAMPLE
# try:
#     driver.get(url)
#
#     # Ожидаем появления контейнеров
#     containers = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "container")))
#
#     for index, container in enumerate(containers, start=1):
#
#         # Дожидаемся, когда чекбокс станет выбранным
#         checkbox = container.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
#         wait.until(EC.element_to_be_selected((checkbox)))
#
#         # Кликаем на кнопку "Проверить"
#         button = container.find_element(By.TAG_NAME, "button")
#         button.click()
#
#     # Получаем и выводим сообщение
#     result_message = wait.until(EC.visibility_of_element_located((By.ID, "result")))
#     print(result_message.text)
#
# finally:
#     driver.quit()

#TASK3
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/6/index.html')
    checkbox = browser.find_element(By.ID,"myCheckbox")
    WebDriverWait(browser, 100).until(EC.element_to_be_selected(checkbox))
    browser.find_element(By.TAG_NAME, "button").click()
    print(browser.find_element(By.TAG_NAME, "p").text)
#EXAMPLE
# try:
#     # Ожидание активации чекбокса
#     checkbox = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "myCheckbox"))
#     )
#
#     # Ожидание активации чекбокса (чекбокс должен быть выбран)
#     WebDriverWait(driver, 10).until(
#         EC.element_located_to_be_selected((By.ID, "myCheckbox"))
#     )
#
#     # Нажатие на кнопку "Проверить"
#     check_button = driver.find_element(By.XPATH, '//button[text()="Проверить"]')
#     check_button.click()
#
#     # Получение значения из <p id="result"></p>
#     result = driver.find_element(By.ID, "result")
#     print(result.text)
#
# finally:
#     driver.quit()

#TASK2
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')
    all_buttons = browser.find_elements(By.CLASS_NAME, "box_button")
    ad = browser.find_element(By.ID,"ad_window")
    button_to_close = browser.find_element(By.ID, "close_ad")
    for but in all_buttons:
        WebDriverWait(browser, 100).until(EC.element_to_be_clickable(but))
        time.sleep(5)
        but.click()
        WebDriverWait(browser, 100).until(EC.visibility_of(button_to_close)).click()
        WebDriverWait(browser, 100).until(EC.invisibility_of_element_located(ad))
    str_text = ""
    for but in all_buttons:
        str_text += but.text + "-"
    print(str_text)

#EXAMPLE
# with webdriver.Chrome() as driver:
#     driver.set_window_size(1200, 800)
#     driver.get("https://parsinger.ru/selenium/5.9/5/index.html")
#     time.sleep(2)
#     locator_ad = (By.ID, "ad_window")
#     locator_close = (By.ID, "close_ad")
#     answers = [""] * 9
#     for btn in driver.find_elements(By.CLASS_NAME, "box_button"):
#         WebDriverWait(driver, 30).until(
#             EC.element_to_be_clickable(btn)
#         ).click()
#         WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable(locator_close)
#         ).click()
#         WebDriverWait(driver, 30).until(
#             EC.invisibility_of_element_located(locator_ad)
#         )
#         WebDriverWait(driver, 10).until(lambda x: btn.text != "")
#         idx = int(btn.get_attribute("data-index"))
#         answers[idx] = btn.text
#
#     print("-".join(answers))
#TASK1
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/4/index.html')
    browser.find_element(By.CLASS_NAME,"close").click()
    element = browser.find_element(By.ID, 'ad')
    WebDriverWait(browser, 100).until(EC.invisibility_of_element_located(element))
    browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(10)

#EXAMPLE
# # Запуск браузера и открытие страницы
# driver = webdriver.Chrome()
# driver.get("https://parsinger.ru/selenium/5.9/4/index.html")
#
# # Ожидание загрузки страницы
# time.sleep(2)
#
# # Нажатие на крестик для закрытия рекламного окна
# close_button = driver.find_element(By.CSS_SELECTOR, "#ad .close")
# close_button.click()
#
# # Ожидание исчезновения рекламного окна
# wait = WebDriverWait(driver, 10)
# ad = driver.find_element(By.ID, "ad")
# wait.until(EC.invisibility_of_element_located((By.ID, "ad")))
#
# # Нажатие на кнопку "Нажми на меня"
# button = driver.find_element(By.CSS_SELECTOR, "button[onclick='showSecretNumber()']")
# button.click()
#
# # Извлечение значения из тега <p>
# message = driver.find_element(By.ID, "message").text
# print("Секретное сообщение:", message)
#
# # Закрытие браузера
# driver.quit()