import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#TASK2
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/4/index.html')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    WebDriverWait(browser, 40).until(EC.title_contains("JK8HQ"))
    print(browser.execute_script("return document.title;"))

#TASK1
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/3/index.html')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    WebDriverWait(browser, 40).until(EC.title_is("345FDG3245SFD"))
    print(browser.find_element(By.ID, "result").text)

#URL METHODS
# from selenium.webdriver.support import expected_conditions as EC
# EC.title_is(title: str) Это ожидаемое условие, которое проверяет, совпадает ли текущий заголовок веб-страницы с предоставленным значением.
# EC.title_contains(title: str) Это ожидаемое условие, которое проверяет, содержит ли текущий заголовок веб-страницы заданное подстроковое значение.
# EC.url_contains(url: str)
        # # Допустим, у вас есть следующая ссылка (URL) на веб-сайт:
        # https://www.example.com/dashboard/
        #
        # #Если вы используете метод EC.url_contains("dashboard"), он вернет True для этой ссылки, потому что строка "dashboard" содержится в URL.
        #
        # # Ожидание, пока URL будет содержать "dashboard"
        # WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
# EC.url_matches(pattern: str)
        # # Ожидание, пока URL соответствует шаблону
        # WebDriverWait(driver, 10).until(EC.url_matches(r"https://www\.example\.com/[0-9]{4}/"))
# EC.url_to_be(url: str) Это ожидаемое условие, которое убеждается, что текущий URL веб-страницы точно совпадает с предоставленным значением.
#         # Ожидание, пока URL станет "https://www.example.com"
#         WebDriverWait(driver, 10).until(EC.url_to_be("https://www.example.com"))
# EC.url_changes(url: str) Это условие сравнивает текущий URL страницы с предоставленным значением. Если они не совпадают, условие считается выполненным.
#         # Ожидание, пока URL изменится относительно "https://www.example.com"
#         WebDriverWait(driver, 10).until(EC.url_changes("https://www.example.com"))

# Почему необходимо использовать Implicit Wait?
# Простота: Это простой способ убедиться, что ваш код будет ждать достаточное количество времени перед тем как продолжить выполнение.
# Глобальность: Один раз установив, он применяется ко всем последующим операциям поиска.

#IMPLICIT WAIT FOR ALL ACTIONS
driver.implicitly_wait(2)
driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
driver.find_element(By.ID, "adder").click()
added = driver.find_element(By.ID, "box0")

#WAIT FOR ACTIVE EXPLICIT
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/1/index.html')
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    time.sleep(3)
    print(browser.find_element(By.ID, 'result').text)


# WebDriverWait(browser, poll_frequency=0.5, timeout=10).until(EC.element_to_be_clickable((By.ID, "btn")))
# Параметры WebDriverWait:
# browser: Экземпляр WebDriver (например, Ie, Firefox, Chrome или Remote)
#
# poll_frequency=float: (необязательный): Интервал ожидания между попытками. По умолчанию равен значению 0.5 секунды.
#
# timeout=float: Время ожидания в секундах до таймаута
#
# .until(method): Ожидает, пока предоставленный method вернет что-либо, кроме False. Если method продолжает возвращать False после истечения времени ожидания, будет вызвано исключение TimeoutException.
#
# .until_not(method): Ожидает, пока предоставленный method не вернет False. Если метод не вернет False до истечения времени ожидания, будет вызвано исключение TimeoutException.