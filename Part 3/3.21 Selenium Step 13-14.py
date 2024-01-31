import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#TASK2
with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/selenium/5.7/4/index.html')
    time.sleep(1)
    div = webdriver.find_elements(By.TAG_NAME, 'input')[-1]
    actions = ActionChains(webdriver)
    all_spans = webdriver.find_elements(By.TAG_NAME, "input")
    while True:
        webdriver.execute_script("arguments[0].scrollIntoView(true);", div)
        div = webdriver.find_elements(By.TAG_NAME, 'input')[-1]
        time.sleep(1)
        if len(webdriver.find_elements(By.TAG_NAME, "input")) == len(all_spans):
            break
        else:
            all_spans = webdriver.find_elements(By.TAG_NAME, "input")
    for p in all_spans:
        if int(p.get_attribute("value")) % 2 == 0:
            webdriver.execute_script("arguments[0].scrollIntoView(true);", p)
            p.click()
    time.sleep(30)
#EXAMPLE
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/5.7/4/index.html")
#     child_cont = browser.find_element(By.CSS_SELECTOR, 'div.child_container')
#     while True:
#         ActionChains(browser).scroll_to_element(child_cont).perform()
#         elements = child_cont.find_elements(By.TAG_NAME, 'input')
#         for checkbox in elements:
#             if not int(checkbox.get_attribute("value")) % 2:
#                 checkbox.click()
#         try:
#             # поиск следующего элемента для скроллинга к нему на следующей итерации
#             child_cont = child_cont.find_element(By.XPATH, 'following-sibling::div[@class="child_container"]')
#         except:
#             break # Когда элементы кончатся, выходим из цикла
#     alert_button = browser.find_element(By.CSS_SELECTOR, ".alert_button")
#     ActionChains(browser).scroll_to_element(alert_button).perform()
#     alert_button.click()
#     print(browser.switch_to.alert.text)

#TASK1
with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/infiniti_scroll_3/')
    divs = webdriver.find_elements(By.CSS_SELECTOR, 'div[style*="width"]')
    time.sleep(2)
    actions = ActionChains(webdriver)
    all_spans = webdriver.find_elements(By.TAG_NAME, "span")
    for div in divs:
        while True:
            actions.move_to_element(div).scroll_by_amount(delta_x=0, delta_y=100).perform()
            time.sleep(1)
            if len(webdriver.find_elements(By.TAG_NAME, "span")) == len(all_spans):
                break
            else:
                all_spans = webdriver.find_elements(By.TAG_NAME, "span")
    summary = 0
    for p in all_spans:
        if p.text.isdigit():
            summary += int(p.text)
    print(summary)

#EXAMPLE TASK1
# start = time.time()
# url = 'http://parsinger.ru/infiniti_scroll_3/'
#
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_extension('coordinates.crx')
# result = []
#
# with webdriver.Chrome(options=options_chrome) as browser:
#     browser.get(url)
#     browser.set_window_size(1024, 720)
#
#     while True:
#         ActionChains(browser).scroll(85, 275, 85, 275).perform()
#         ActionChains(browser).scroll(280, 300, 280, 300).perform()
#         ActionChains(browser).scroll(480, 300, 480, 300).perform()
#         ActionChains(browser).scroll(680, 320, 680, 320).perform()
#         ActionChains(browser).scroll(900, 300, 900, 300).perform()
#
#         catch_last_elem = [x for x in browser.find_element(By.ID, 'scroll-container_5').find_elements(By.TAG_NAME, 'span') if x.get_attribute('class')]
#         if catch_last_elem:
#             [result.append(int(x.text)) for x in browser.find_element(By.CLASS_NAME, 'main').find_elements(By.TAG_NAME, 'span')]
#             break
#
# print(sum(result))
# print(f'Time is running{time.time() - start}')

#ЧАСТИЧНОЕ СОВПАДЕНИЕ ID
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_3/')
#     containers = browser.find_elements(By.XPATH, '//div[contains(@id, "scroll-container")]')
#     s = 0
#     for container in containers:
#         while not container.find_elements(By.CLASS_NAME, 'last-of-list'):
#             ActionChains(browser).move_to_element(container.find_element(By.TAG_NAME, 'div')).scroll_by_amount(0, 500).perform()
#         s += sum(int(span.text) for span in container.find_elements(By.TAG_NAME, 'span'))
#     print(s)