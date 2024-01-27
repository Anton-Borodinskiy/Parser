import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#TASK6
url = 'https://parsinger.ru/selenium/5.5/5/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(2)
    all_divs = browser.find_elements(By.TAG_NAME, "div")
    for div in all_divs:
        if "background-color" in div.get_attribute("style"):
            color = div.find_element(By.TAG_NAME, "span").text
            all_options = div.find_elements(By.TAG_NAME, "option")
            for option in all_options:
                if option.text == color:
                    option.click()
            all_buttons = div.find_elements(By.TAG_NAME, "button")
            for but in all_buttons:
                if but.get_attribute("data-hex") == color:
                    but.click()
            checkbox = div.find_element(By.CSS_SELECTOR, '[type=checkbox]').click()
            text = div.find_element(By.CSS_SELECTOR, '[type=text]').send_keys(color)
            all_buttons[-1].click()
    find_last_button = browser.find_elements(By.TAG_NAME, "button")[-1].click()
    time.sleep(15)
#EXAMPLE1
# def main():
#     with webdriver.Chrome() as driver:
#         driver.get("https://parsinger.ru/selenium/5.5/5/1.html")
#
#         divs = driver.find_elements(By.CSS_SELECTOR, "#main-container > div")
#
#         for div in divs:
#             # Получаем HEX цвет
#             color_span = div.find_element(By.TAG_NAME, "span")
#             hex_color = color_span.text
#
#             # Выбираем цвет в выпадающем списке
#             dropdown = Select(div.find_element(By.TAG_NAME, "select"))
#             dropdown.select_by_visible_text(hex_color)
#
#             # Нажимаем на кнопку с атрибутом data-hex
#             button = div.find_element(By.CSS_SELECTOR, f'button[data-hex="{hex_color}"]')
#             button.click()
#
#             # Ставим чекбокс
#             checkbox = div.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
#             checkbox.click()
#
#             # Вставляем HEX цвет в текстовое поле
#             text_field = div.find_element(By.CSS_SELECTOR, "input[type='text']")
#             text_field.send_keys(hex_color)
#
#             # Нажимаем кнопку "Проверить"
#             check_button = div.find_element(By.XPATH, ".//button[text()='Проверить']")
#             check_button.click()
#
#         # Нажимаем кнопку "Проверить все элементы"
#         check_all_button = driver.find_element(By.XPATH, "//button[text()='Проверить все элементы']")
#         check_all_button.click()
#
#         # Получаем и выводим текст алерта
#         alert = Alert(driver)
#         print(alert.text)
#         alert.accept()
#
#
# if __name__ == "__main__":
#     main()

#EXAMPLE2
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
#     for i in browser.find_elements(By.CSS_SELECTOR, 'div[style*="background-color"]'):
#         nice_color = i.find_element(By.CSS_SELECTOR, 'span').text
#         color_dropdown = Select(i.find_element(By.CSS_SELECTOR, 'select'))
#         color_dropdown.select_by_visible_text(nice_color)
#         i.find_element(By.CSS_SELECTOR, f'div button[data-hex="{nice_color}"]').click()
#         i.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
#         i.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(nice_color)
#         i.find_elements(By.CSS_SELECTOR, 'button')[-1].click()
#     browser.find_element(By.CSS_SELECTOR, 'body>button').click()
#     print(browser.switch_to.alert.text)

#TASK5
url = 'https://parsinger.ru/selenium/5.5/4/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(2)
    all_to_clear = browser.find_element(By.ID, "main-containermain-container")
    for div in all_to_clear:
        all_text_area = div.find_elements(By.TAG_NAME,"textarea")
        adder = all_text_area[1].send_keys(all_text_area[0].text)
        cleaner = all_text_area[0].clear()
        div.find_element(By.TAG_NAME,"button").click()
        print(1)
    button = browser.find_element(By.ID, 'checkAll').click()
    time.sleep(10)


# gray = c.find_element(By.XPATH, ".//textarea[@color='gray']")
# blue = c.find_element(By.XPATH, ".//textarea[@color='blue']")

# url = "https://parsinger.ru/selenium/5.5/4/1.html"
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     parents = browser.find_elements(By.CLASS_NAME, 'parent')
#     for parent in parents:
#         gray = parent.find_element(By.CSS_SELECTOR, '[color=gray]')
#         blue = parent.find_element(By.CSS_SELECTOR, '[color=blue]')
#         blue.send_keys(gray.text)
#         gray.clear()
#         parent.find_element(By.CSS_SELECTOR, 'button').click()
#     browser.find_element(By.ID, 'checkAll').click()
#     time.sleep(10)