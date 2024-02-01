import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
#TASK4 FRAME
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/5/index.html')
    iframes = browser.find_elements(By.TAG_NAME, 'iframe')
    ps = []
    for iframe in iframes:
        browser.switch_to.frame(iframe)
        browser.find_element(By.CSS_SELECTOR, 'button[onclick="showNumber()"]').click()
        ps.append(browser.find_element(By.ID, "numberDisplay").text)
        browser.switch_to.default_content()
    for p in ps:
        browser.find_element(By.ID, 'guessInput').send_keys(p)
        browser.find_element(By.ID, 'checkBtn').click()
        time.sleep(5)
        browser.find_element(By.ID, 'guessInput').clear()
#EXAMPLE
# with webdriver.Chrome() as driver:
#     driver.get(URL)
#
#     # Перебор всех iframe
#     for i in range(1, 10):
#         time.sleep(2)  # Задержка перед переключением на iframe
#
#         # Переход в iframe
#         iframe = driver.find_element(By.ID, f'iframe{i}')
#         driver.switch_to.frame(iframe)
#
#         # Нажатие на кнопку
#         button = driver.find_element(By.XPATH, "//button[contains(text(),'Нажми меня')]")
#         button.click()
#
#         # Получение числа
#         time.sleep(1)  # Задержка перед чтением числа
#         number = driver.find_element(By.ID, 'numberDisplay')
#         number_value = number.text
#
#         # Возврат к основному содержимому
#         driver.switch_to.default_content()
#
#         # Ввод числа в поле и нажатие кнопки
#         input_field = driver.find_element(By.ID, 'guessInput')
#         input_field.clear()
#         input_field.send_keys(number_value)
#
#         check_btn = driver.find_element(By.ID, 'checkBtn')
#         check_btn.click()
#
#         try:
#             # Получение текста из alert
#             time.sleep(1)  # Задержка перед проверкой наличия alert
#             alert = Alert(driver)
#             print(alert.text)
#             alert.accept()
#             break
#         except NoAlertPresentException:
#             # Если alert не появляется, продолжаем со следующим iframe
#             continue
#
#         time.sleep(2)  # Задержка перед переключением на следующий iframe

#TASK3
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
    buttons = browser.find_elements(By.CLASS_NAME, 'pin')
    for span in buttons:
        text_to_send = span.text
        browser.find_element(By.ID, "check").click()
        prompt = browser.switch_to.alert
        prompt.send_keys(text_to_send)
        prompt.accept()
        if len(browser.find_element(By.ID, "result").text) > 0 and "Неверный" not in browser.find_element(By.ID, "result").text:
            time.sleep(0.5)
            print(browser.find_element(By.ID, "result").text)
            break
        else:
            continue
#EXAMPLE
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/blank/modal/4/index.html')
#     pin_code = [x.text for x in browser.find_elements(By.CLASS_NAME, 'pin')]
#     for pin in pin_code:
#         browser.find_element(By.ID, 'check').click()
#         confirm = browser.switch_to.alert
#         time.sleep(.3)
#         confirm.send_keys(pin)
#         confirm.accept()
#         result = browser.find_element(By.ID, 'result').text
#         if result.isdigit():
#             print(result)

#TASK2
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/2/index.html')
    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
    for but in buttons:
        but.click()
        alert = browser.switch_to.alert  # Если вы планируете что-то делать с этим событием, можно добавить его в переменную
        code = alert.text
        alert.accept()
        browser.find_element(By.ID, "input").send_keys(code)
        browser.find_element(By.ID, "check").click()
        if len(browser.find_element(By.ID, "result").text) > 0 and "Неверный" not in browser.find_element(By.ID, "result").text:
            time.sleep(0.5)
            print(browser.find_element(By.ID, "result").text)
            break
        else:
            time.sleep(0.5)
            browser.find_element(By.ID, "input").clear()

#TASK1
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
    for but in buttons:
        but.click()
        alert = browser.switch_to.alert  # Если вы планируете что-то делать с этим событием, можно добавить его в переменную
        time.sleep(0.5)
        alert.accept()
        time.sleep(0.5)
        if len(browser.find_element(By.ID, "result").text) > 0:
            print(browser.find_element(By.ID, "result").text)
            break
        else:
            continue

