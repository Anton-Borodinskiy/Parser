import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://parsinger.ru/html/watch/1/1_1.html')
button = browser.find_element(By.ID, "sale_button").click()

time.sleep(10)


# element = driver.find_element(By.ID, "some_id")
# elements = driver.find_elements(By.CSS_SELECTOR, ".some_class")
# element = driver.find_element(By.XPATH, "//div[@attribute='value']")
# element = driver.find_element(By.NAME, "username")
# images = driver.find_elements(By.TAG_NAME, "img")
# buttons = driver.find_elements(By.CLASS_NAME, "btn")
# element = driver.find_element(By.LINK_TEXT, "Continue")
# element = driver.find_element(By.PARTIAL_LINK_TEXT, "Cont")

# # Ищем элемент с тегом img
# elements = driver.find_element(By.TAG_NAME, 'img')
#
# # Ищем все элементы с классом some_class
# elements = driver.find_elements(By.CLASS_NAME, 'some_class')