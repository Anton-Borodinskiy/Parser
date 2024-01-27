#TASK4
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    forms = browser.find_elements(By.XPATH, "//p[2]")
    all_sum = 0
    for form in forms:
        all_sum += int(form.text)
    print(all_sum)
    time.sleep(15)
# with webdriver.Chrome() as browser:
#     browser.get('https://stepik-parsing.ru/selenium/3/3.html')
#     print(sum([int(x.text) for x in browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")]))

#TASK3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    forms = browser.find_elements(By.TAG_NAME, "p")
    all_sum = 0
    for form in forms:
        all_sum += int(form.text)
    print(all_sum)
    time.sleep(15)

# with webdriver.Chrome() as browser:
#     browser.get('https://stepik-parsing.ru/selenium/3/3.html')
#
#     result = [int(x.text) for x in browser.find_elements(By.XPATH, "//div[@class='text']/p")]
#     print(sum(result))

#TASK2
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/2/2.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    forms = browser.find_element(By.PARTIAL_LINK_TEXT, "16243162441624")
    browser.get(forms.get_attribute("href"))
    forms = browser.find_element(By.XPATH, '//p[@id="result"]')
    print(forms.text)


#EXAMPLE
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     browser.find_element(By.LINK_TEXT, '16243162441624').click()
#     result = browser.find_element(By.ID, 'result').text
#     print(result)
#     input()


#TASK1
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/1/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    forms = browser.find_elements(By.CLASS_NAME, 'form')
    for form in forms:
        send_input = form.send_keys('Текст')
    button = browser.find_element(By.CLASS_NAME, 'btn').click()


#BEST EXAMPLE
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_forms = browser.find_elements(By.CLASS_NAME, 'form')
    list_names = browser.find_elements(By.TAG_NAME, 'input')
    for form, text in zip(input_forms, list_names):
        form.send_keys('Текст')
    button = browser.find_element(By.ID, "btn").click()
    secret_code = browser.find_element(By.ID, 'result').text
    print(secret_code)

