import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#TASK8
url = 'https://parsinger.ru/selenium/6/6.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    math_example = browser.find_element(By.ID, "text_box")
    finder = eval(math_example.text)
    boxes =  browser.find_elements(By.TAG_NAME, 'option')
    for form in boxes:
        if int(form.text) == finder:
            form.click()
    button = browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(5)


#TASK7

url = 'https://parsinger.ru/selenium/7/7.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    boxes =  browser.find_elements(By.TAG_NAME, 'option')
    all_sum = 0
    for form in boxes:
        all_sum += int(form.text)
    browser.find_element(By.ID, "input_result").send_keys(str(all_sum))
    button = browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(5)

# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/selenium/7/7.html')
#     options = browser.find_elements(By.TAG_NAME, 'option')
#     res = sum([int(i.text) for i in options])
#     inpt_res = browser.find_element(By.ID, 'input_result').send_keys(res)
#     browser.find_element(By.ID, 'sendbutton').click()
#     time.sleep(10)
