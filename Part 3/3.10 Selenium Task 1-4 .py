import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#TASK4
url = 'https://parsinger.ru/selenium/5.5/3/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    all_to_clear = browser.find_elements(By.CLASS_NAME, "parent")
    all_sum = 0
    for box in all_to_clear:
        if box.find_element(By.CLASS_NAME, "checkbox").is_selected():
            all_sum += int(box.text)
    print(all_sum)
#EX1
# # Инициализация драйвера
# driver = webdriver.Chrome()
#
# # Открыть HTML-файл
# driver.get("https://parsinger.ru/selenium/5.5/3/1.html")
#
# # Ждем, пока все элементы прогрузятся
# time.sleep(2)
#
# # Список для хранения собранных чисел
# collected_numbers = []
#
# # Находим все родительские элементы
# parents = driver.find_elements(By.CLASS_NAME, 'parent')
#
# # Проходимся по каждому родительскому элементу
# for parent in parents:
#     # Находим textarea и checkbox внутри родительского элемента
#     textarea = parent.find_element(By.TAG_NAME, 'textarea')
#     checkbox = parent.find_element(By.CLASS_NAME, 'checkbox')
#
#     # Проверяем, включен ли чекбокс
#     if checkbox.is_selected():
#         # Добавляем число из textarea в список
#         collected_numbers.append(int(textarea.get_attribute("value")))
#
# # Выводим собранные числа
# print("Собранные числа: ", collected_numbers,sum(collected_numbers))
#
# # Закрываем браузер
# driver.quit()

#EX2
# with webdriver.Chrome() as browser:
#     browser.get(url='https://parsinger.ru/selenium/5.5/3/1.html')
#     all_boxes = browser.find_elements(By.CLASS_NAME, 'parent')
#     res = sum(map(lambda el: int(el.text), filter(lambda el: el.find_element(By.CLASS_NAME, 'checkbox').is_selected(), all_boxes)))
#     print(res)


#TASK3
url = 'https://parsinger.ru/selenium/5.5/2/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    all_to_clear = browser.find_elements(By.CLASS_NAME, "text-field")
    for one in all_to_clear:
        if one.is_enabled():
            one.clear()
        else:
            continue
    browser.find_element(By.ID,"checkButton").click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)



# with webdriver.Chrome() as driver:
#     driver.get("https://parsinger.ru/selenium/5.5/2/1.html")
#
#     # Ждем 1 секунду, чтобы страница полностью прогрузилась
#     time.sleep(1)
#
#
#     # Находим все текстовые поля на странице
#     text_fields = driver.find_elements(By.CSS_SELECTOR, ".text-field")
#
#     # Проходимся по каждому текстовому полю и очищаем его, если оно не заблокировано
#     for field in text_fields:
#         if not field.get_attribute('disabled'):
#             field.clear()
#
#     # Находим кнопку "Проверить" и кликаем по ней
#     check_button = driver.find_element(By.ID, "checkButton")
#
#     # Проверка, заблокирована ли кнопка
#     if not check_button.get_attribute('disabled'):
#         check_button.click()
#     else:
#         print("Кнопка 'Проверить' заблокирована.")
#
#     time.sleep(2)
#     # Переключаемся на алерт
#     alert = driver.switch_to.alert
#
#     # Получаем текст с алерта
#     alert_text = alert.text
#
#     # Выводим текст алерта
#     print(f"Текст алерта: {alert_text}")

#TASK2
url = 'https://parsinger.ru/selenium/5.5/1/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    all_to_clear = browser.find_elements(By.CLASS_NAME, "text-field")
    for one in all_to_clear:
        one.clear()
    browser.find_element(By.ID,"checkButton").click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
# with webdriver.Chrome() as driver:
#     driver.get("https://parsinger.ru/selenium/5.5/1/1.html")
#
#     # Ждем 1 секунду, чтобы страница полностью прогрузилась
#     time.sleep(1)
#
#     # Находим все текстовые поля на странице
#     text_fields = driver.find_elements(By.CSS_SELECTOR, ".text-field")
#
#     # Очищаем каждое текстовое поле
#     for field in text_fields:
#         field.clear()
#
#     # Находим кнопку "Проверить" и нажимаем на нее
#     check_button = driver.find_element(By.ID, "checkButton")
#     check_button.click()
#
#     # Ждем появления алерта
#     time.sleep(1)
#
#     # Переключаемся на алерт
#     alert = driver.switch_to.alert
#
#     # Получаем текст с алерта
#     alert_text = alert.text
#
#     # Выводим текст алерта
#     print(f"Текст алерта: {alert_text}")
#
#     # Закрыть алерт
#     alert.accept()


#####################
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/5.5/1/1.html")
#
#     for elem in browser.find_elements(By.TAG_NAME, "input"):
#         elem.clear()
#
#     browser.find_element(By.ID, "checkButton").click()
#
#     alert = browser.switch_to.alert
#
#     with open("output.txt", "w", encoding="utf-8") as file_output:
#         print(alert.text, file=file_output)

#TASK1
url = 'https://parsinger.ru/methods/1/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    while(True):
        if "refresh page" != browser.find_element(By.ID, "result").text:
            print(browser.find_element(By.ID, "result").text)
            break
        else:
            browser.refresh()
        time.sleep(1)

# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/methods/1/index.html')
#     while browser.find_element(By.ID, 'result').text == 'refresh page':
#         browser.refresh()
#     print(browser.find_element(By.ID, 'result').text)
############
# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://parsinger.ru/methods/1/index.html')
#     while True:
#         res = webdriver.find_element(By.ID, 'result').text
#         webdriver.refresh()
#         if res.isdigit():
#             print(res)
#             break

