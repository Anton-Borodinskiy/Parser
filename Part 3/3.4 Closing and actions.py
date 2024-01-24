import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get('http://parsinger.ru/html/watch/1/1_1.html')
button = driver.find_element(By.ID, "sale_button")
time.sleep(2)
button.click()
time.sleep(2)
driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    driver= webdriver.Chrome()
    driver.get('http://parsinger.ru/html/watch/1/1_1.html')
    button = driver.find_element(By.ID, "sale_button")
    time.sleep(2)
    button.click()
    time.sleep(2)
finally:
    driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('http://parsinger.ru/html/watch/1/1_1.html')
    button = driver.find_element(By.ID, "sale_button")
    time.sleep(2)
    button.click()
    time.sleep(2)


# driver.close() - закрывает текущее окно браузера, если во время работы вы открыли новое окно или вкладку.
#
# driver.quit() - закрывает все окна, вкладки, процессы веб-драйвера, которые были запущены во время сессии.


#ACTIONS ##############
# browser.find_element(By.ID, "some_button_id").click()
# browser.find_element(By.NAME, "some_textbox_name").send_keys("Hello, World!")
# browser.find_element(By.TAG_NAME, "a").get_attribute("href")
# browser.find_element(By.CLASS_NAME, "some_class_name").text