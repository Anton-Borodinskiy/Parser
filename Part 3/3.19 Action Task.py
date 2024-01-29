import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/selenium/5.7/5/index.html')
    all_btn = webdriver.find_elements(By.TAG_NAME,"button")
    for btn in all_btn:
        webdriver.execute_script("return arguments[0].scrollIntoView(true);", btn)
        btn.click()
    for btn in all_btn:
        print(btn.text)
        actions = ActionChains(webdriver)
        actions.click_and_hold(btn).pause(float(btn.text)).release(btn).perform()
    alert = webdriver.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()
    time.sleep(20)
