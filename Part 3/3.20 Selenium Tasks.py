import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#TASK3
with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/infiniti_scroll_2/')
    time.sleep(2)
    div = webdriver.find_element(By.ID, 'scroll-container').find_element(By.TAG_NAME, "div")
    all_spans = webdriver.find_elements(By.TAG_NAME, "p")
    actions = ActionChains(webdriver)
    while True:
        actions.move_to_element(div).scroll_by_amount(delta_x=0, delta_y=100).perform()
        time.sleep(1)
        if len(webdriver.find_elements(By.TAG_NAME, "p")) == len(all_spans):
            break
        else:
            all_spans = webdriver.find_elements(By.TAG_NAME, "p")
    summary = 0
    for p in all_spans:
        if p.text.isdigit():
            summary += int(p.text)
    print(summary)
#EXAMPLE
# with webdriver.Chrome() as browser:
#     url = 'http://parsinger.ru/infiniti_scroll_2/'
#     browser.get(url)
#     browser.set_window_size(1920, 1080)
#     while True:
#         ActionChains(browser).scroll(800, 400, 800, 400).perform()
#         time.sleep(0.2)
#         attrbt = [x.get_attribute('id') for x in browser.find_elements(By.TAG_NAME, 'p') if x.get_attribute('class')]
#         if attrbt:
#             break
#     res = [int(x.text) for x in browser.find_elements(By.TAG_NAME, 'p') if x.text]
#     print(sum(res))

#EXAMPLE2
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_2/')
#     div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
#
#     for _ in range(10):
#         ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
#
#     print(sum(int(span.text) for span in browser.find_elements(By.CSS_SELECTOR, '#scroll-container p')))
#     time.sleep(5)

#TASK2
with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/infiniti_scroll_1/')
    time.sleep(2)
    div = webdriver.find_element(By.ID, 'scroll-container').find_element(By.TAG_NAME, "div")
    print(div.text)
    actions = ActionChains(webdriver)
    while True:
        try:
            actions.move_to_element(div).scroll_by_amount(delta_x=0, delta_y=100).perform()
            time.sleep(1)
            if len(webdriver.find_elements(By.CLASS_NAME, "last-of-list")) > 0:
                break
        except:
            break
    spans = webdriver.find_elements(By.TAG_NAME, "span")
    summary = 0
    for span in spans:
        if span.text.isdigit():
            summary += int(span.text)
    print(summary)
#EXAMPLE1
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     time.sleep(0.5)
#     count = 0
#     checking = []
#     result = []
#     while True:
#         input_list = [x for x in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'input')]
#
#         for inp in input_list:
#             if inp not in checking:
#                 inp.send_keys(Keys.DOWN)
#                 count += 1
#                 checking.append(inp)
#
#
#         break_loop = [x for x in browser.find_elements(By.TAG_NAME, 'span') if x.get_attribute('class')]
#         if break_loop:
#             break
#     span_list = [result.append(int(x.text)) for x in
#                  browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span')]
#     print(f'Результат: {sum(result)}')

#EXAMPLE2
# with (webdriver.Chrome() as browser):
#     browser.get('https://parsinger.ru/infiniti_scroll_1/')
#     div = browser.find_element(By.CSS_SELECTOR, '#scroll-container > div')
#     actions = ActionChains(browser)
#     result_list = []
#     result = 0
#     flag = True
#     while flag:
#         actions(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
#         for el in browser.find_elements(By.CSS_SELECTOR, '#scroll-container > span'):
#             if el not in result_list:
#                 result += int(el.text)
#                 result_list.append(el)
#                 if el.get_attribute('class') == 'last-of-list':
#                     flag = False
#     print(result)

#TASK1
with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/scroll/2/index.html')
    all_checkbox = webdriver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
    for check in all_checkbox:
        webdriver.execute_script("return arguments[0].scrollIntoView(true);", check)
        check.click()
    all_span = webdriver.find_elements(By.CSS_SELECTOR, 'span[id*="result"]')
    summary = 0
    for span in all_span:
        if len(span.text.strip()) == 0:
            pass
        else:
            summary += int(span.text)

    print(summary)
#EXAMPLE
#     with webdriver.Chrome() as browser:
#         browser.get('http://parsinger.ru/scroll/2/')
#
#         for tag_input in browser.find_elements(By.TAG_NAME, 'input'):
#             tag_input.click()
#
#         for x in browser.find_elements(By.TAG_NAME, 'span'):
#             if x.text.isdigit():
#                 result.append(int(x.text))
# print(sum(result))