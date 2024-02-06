import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
#TASK8
with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/selenium/5.10/6/index.html")
    sliders = driver.find_elements(By.CLASS_NAME, "slider-container")
    actions = ActionChains(driver)
    for slider in sliders:
        current = slider.find_element(By.CLASS_NAME, "current-value").text
        target = slider.find_element(By.CLASS_NAME, "target-value").text
        if int(target) < int(current):
            while int(target) != int(slider.find_element(By.CLASS_NAME, "current-value").text):
                slider.find_element(By.CLASS_NAME, "volume-slider").send_keys(Keys.ARROW_LEFT)
        else:
            while int(target) != int(slider.find_element(By.CLASS_NAME, "current-value").text):
                slider.find_element(By.CLASS_NAME, "volume-slider").send_keys(Keys.ARROW_RIGHT)

    time.sleep(20)
#EXAMPLE
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/5.10/6/index.html')
#     cases = driver.find_elements(By.CLASS_NAME, 'slider-container')
#     for case in cases:
#         target_value = int(case.find_element(By.CLASS_NAME, 'target-value').text)
#         slider = case.find_element(By.TAG_NAME, 'input')
#         delta = target_value - int(slider.get_attribute("value"))
#
#         if delta < 0:
#             action_function = Keys.ARROW_LEFT
#         else:
#             action_function = Keys.ARROW_RIGHT
#
#         for _ in range(abs(delta)):
#             slider.send_keys(action_function)
#
#     print(driver.find_element(By.ID, 'message').text)


#TASK7
with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/selenium/5.10/8/index.html")
    time.sleep(2)
    pieces = driver.find_elements(By.CLASS_NAME, "piece")
    drops = driver.find_elements(By.CLASS_NAME, "range")
    actions = ActionChains(driver)
    for i in range(len(pieces)):
        actions.click_and_hold(pieces[i]).perform()
        actions.move_by_offset(int(drops[i].get_attribute("id").split("_")[-1]), 0).perform()
        time.sleep(0.1)
        actions.release().perform()
    time.sleep(20)

#EXAMPLE
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# url = 'https://parsinger.ru/selenium/5.10/8/index.html'
#
# with webdriver.Chrome() as driver:
#     driver.get(url)
#
#     # Ожидание загрузки страницы
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'content'))
#     )
#
#     for i in range(1, 9):  # Перебор всех piece и range с 1 до 8
#         piece_id = f'piece_{i}00'
#         range_id = f'range_{i}00'
#
#         piece_element = driver.find_element(By.ID, piece_id)
#         range_element = driver.find_element(By.ID, range_id)
#
#         # Получение расстояния из текста внутри тега <p> в range_
#         distance_text = range_element.find_element(By.TAG_NAME, 'p').text
#         distance = int(distance_text.split(': ')[1].replace('px', ''))
#
#         # Перемещение piece в range_ с помощью .move_by_offset()
#         action = ActionChains(driver)
#         action.drag_and_drop_by_offset(piece_element, distance, 0).perform()  # Обновлено смещение по оси x
#
#     # Ожидание появления сообщения
#     message = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'message'))
#     )
#
#     print(message.text)  # Вывод сообщения

#TASK6
with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/selenium/5.10/4/index.html")
    time.sleep(2)
    blocks = driver.find_elements(By.CLASS_NAME, "ball_color")
    end = driver.find_elements(By.CLASS_NAME, "basket_color")
    for block in blocks:
        for en in end:
            if en.get_attribute("class").split()[1] in block.get_attribute("class"):
                ActionChains(driver).drag_and_drop(block, en).perform()
                time.sleep(0.5)
    time.sleep(20)

#EXAMPLE
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
# with webdriver.Chrome() as driver:
#     driver.get("https://parsinger.ru/selenium/5.10/4/index.html")
#
#     driver.implicitly_wait(10)
#
#     balls = driver.find_elements(By.CLASS_NAME, "ball_color")
#     baskets = {color: driver.find_element(By.CSS_SELECTOR, f".basket_color.{color}") for color in
#                ["red", "blue", "green", "black"]}
#
#     for ball in balls:
#         color = ball.get_attribute("class").split(" ")[1].replace("_ball", "")
#         basket = baskets[color]
#
#         ActionChains(driver).drag_and_drop(ball, basket).perform()
#
#         time.sleep(0.1)  # небольшая задержка для более плавного перемещения
#
#     message = driver.find_element(By.CLASS_NAME, "message").text
#     print(message)

#TASK5
with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/selenium/5.10/3/index.html")
    blocks = driver.find_elements(By.CLASS_NAME, "draganddrop")
    end = driver.find_elements(By.CLASS_NAME, "draganddrop_end")
    for block in blocks:
        for en in end:
            if en.value_of_css_property("border-color").split("(")[-1].replace(")","") in block.value_of_css_property("background-color").split("(")[-1].replace(")",""):
                ActionChains(driver).drag_and_drop(block, en).perform()
                time.sleep(0.5)

    time.sleep(20)

#TASK4
with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/draganddrop/2/index.html")
    red = driver.find_element(By.ID, "draggable")
    blocks = driver.find_elements(By.CLASS_NAME, "box")
    for block in blocks:
        ActionChains(driver).drag_and_drop(driver.find_element(By.ID, "draggable"), block).perform()
    time.sleep(20)


#TASK3
with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/selenium/5.10/2/index.html")
    blocks = driver.find_elements(By.CLASS_NAME, "draganddrop")
    end = driver.find_element(By.CLASS_NAME, "draganddrop_end")
    for block in blocks:
        ActionChains(driver).drag_and_drop(block, end).perform()
    time.sleep(20)
#EXAMPLE
# with webdriver.Chrome() as browser:
#     browser.get(url)
#
#     for box in browser.find_elements(By.XPATH, '//div[@id="main_container"]/div')[:-1]:
#         ActionChains(browser).click_and_hold(box).move_by_offset(browser.get_window_size()['width'] - 100, 0).perform()
#
#     WebDriverWait(browser, 10).until(lambda _: browser.find_element(By.ID, "message").text != "")
#     print(browser.find_element(By.ID, "message").text)
#TASK2
with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/draganddrop/3/index.html")
    drag_dots = driver.find_elements(By.CLASS_NAME,"controlPoint")
    block_for_move = driver.find_element(By.ID,"block1")
    actions = ActionChains(driver)

    # Нажмите на ползунок и удерживайте кнопку мыши
    actions.click_and_hold(block_for_move).perform()

    # В цикле перемещайте ползунок на 1 единицу
    for _ in range(100):  # пример для 10 шагов
        actions.move_by_offset(10, 0).perform()
        time.sleep(0.1)  # пауза для наглядности

    # Отпустите кнопку мыши
    actions.release().perform()
    time.sleep(20)
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/draganddrop/3/index.html')
#     time.sleep(1)
#     drag = browser.find_element(By.ID, 'block1')
#     actions = ActionChains(browser)
#     lst = [10]*400
#     actions.click_and_hold(drag)
#     for x in lst:
#         actions.move_by_offset(x, 0)
#     actions.perform()
#     time.sleep(5)

#TASK1
with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/draganddrop/1/index.html")
    element_to_drag1 = driver.find_element(By.ID, "draggable")
    element_to_drag2 = driver.find_element(By.ID, "field2")
    ActionChains(driver).drag_and_drop(element_to_drag1, element_to_drag2).perform()
    time.sleep(10)
#EXAMPLE
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/draganddrop/1/index.html')
#     time.sleep(3)
#     drag = browser.find_element(By.XPATH, '//*[@id="draggable"]')
#     final = browser.find_element(By.XPATH, '//*[@id="field2"]')
#     actions = ActionChains(browser)
#
#     actions.drag_and_drop(drag, final).perform()
#     result = browser.find_element(By.ID, 'result').text
#     print(result)