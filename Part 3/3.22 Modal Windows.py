import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    #JUST ALERT
    browser.get('http://parsinger.ru/blank/modal/1/index.html')
    browser.find_element(By.ID, 'alert').click()
    time.sleep(1)
    alert = browser.switch_to.alert # Если вы планируете что-то делать с этим событием, можно добавить его в переменную
    print(alert.text)
    time.sleep(1)
    alert.accept()
    time.sleep(1)
    #PROMPT
    browser.find_element(By.ID, 'prompt').click()
    time.sleep(2)
    prompt = browser.switch_to.alert
    prompt.send_keys('TEST123')
    prompt.accept()
    time.sleep(.5)
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(1)
    #CONFIRM
    browser.find_element(By.ID, 'confirm').click()
    time.sleep(2)
    prompt = browser.switch_to.alert
    prompt.accept() #Замените на .dismiss() чтобы нажать на кнопку "Отмена"
    time.sleep(.5)

# .switch_to - позволяет переключить фокус на модальное окно. Это необходимо, чтобы взаимодействовать с содержимым этого окна.
# Переключение фокуса на модальное окно
driver.switch_to.alert


# .accept() - имитирует нажатие на кнопку "ОК" в модальном окне. Обычно используется для подтверждения какого-либо действия.
# Подтвердить содержимое модального окна
driver.switch_to.alert.accept()

# .dismiss() - имитирует нажатие на кнопку "Отмена" в модальном окне. Позволяет отказаться от выполнения какого-либо действия или закрыть окно без подтверждения.
# Или отклонить содержимое модального окна
driver.switch_to.alert.dismiss()

# .send_keys() - позволяет отправить текст в текстовое поле внутри модального окна. Например, это может быть поле для ввода пароля или комментария.
# Отправка текста в текстовое поле модального окна
driver.switch_to.alert.send_keys("Текст для отправки")

# .text - возвращает заголовок (title) модального окна. Это может пригодиться для проверки того, что правильное окно отображается на экране.
# Получение title модального окна
modal_title = driver.switch_to.alert.text