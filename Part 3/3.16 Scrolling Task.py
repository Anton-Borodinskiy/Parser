import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
#TASK1
with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/scroll/4/index.html')
    all_btn = webdriver.find_elements(By.TAG_NAME,"button")
    sum_all = 0
    for btn in all_btn:
        webdriver.execute_script("return arguments[0].scrollIntoView(true);", btn)
        btn.click()
        sum_all += int(webdriver.find_element(By.ID,"result").text)
    print(sum_all)