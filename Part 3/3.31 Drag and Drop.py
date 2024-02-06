#CLICK AND HOLD
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

url = "https://parsinger.ru/selenium/5.10/7/index.html"

# Инициализация драйвера
with webdriver.Chrome() as driver:
    # Устанавливаем неявное ожидание для всех элементов
    driver.implicitly_wait(10)

    # Переход на страницу
    driver.get(url)
    time.sleep(1)
    # Поиск элемента для перетаскивания и контейнера
    click_and_hold_element = driver.find_element(By.ID, "click_and_hold")
    container = driver.find_element(By.CLASS_NAME, "container")

    # Выполнение операции перетаскивания
    actions = ActionChains(driver)
    actions.click_and_hold(click_and_hold_element).move_to_element(container).release().perform()

    # Даем время для визуальной проверки (по желанию)
    time.sleep(5)

#DROP OFFSET
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/selenium/5.10/7/index.html")
    element_to_drag = driver.find_element(By.ID, "click_and_hold")
    time.sleep(1)
    # Создание объекта ActionChains, инициализация операции перетаскивания элемента на 500 пикселей вправо
    # и выполнение цепочки действий
    ActionChains(driver).drag_and_drop_by_offset(element_to_drag, 500, 0).release().perform()

    time.sleep(10)


#ПЛАВНЫЙ ПОЛЗУНОК
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By

# Использование контекстного менеджера для управления драйвером
with webdriver.Chrome() as driver:
    # Загрузите локальный HTML-файл
    driver.get('https://parsinger.ru/selenium/5.10/5/index.html')

    slider = driver.find_element(By.ID,'volume')
    width = slider.size['width']
    # Вычислите смещение для 1 единицы
    offset = width / 100

    actions = ActionChains(driver)

    # Нажмите на ползунок и удерживайте кнопку мыши
    actions.click_and_hold(slider).perform()

    # В цикле перемещайте ползунок на 1 единицу
    for _ in range(10):  # пример для 10 шагов
        actions.move_by_offset(offset, 0).perform()
        time.sleep(0.1)  # пауза для наглядности

    # Отпустите кнопку мыши
    actions.release().perform()




#
# # action.drag_and_drop(element, target) - это метод класса ActionChains. Он позволяет перетащить element  и поместить его в элемент target.
#
#
# # Находим исходный элемент, который будем перемещать
# element = driver.find_element(By.ID,"source-element")
#
# # Находим целевой элемент, куда будем перемещать иcходный элемент
# target = driver.find_element(By.ID,"target-element")
#
# # Создаём экземпляр класса ActionChains
# actions = ActionChains(driver)
#
# # Выполняем действие перетаскивания
# actions.drag_and_drop(element, target).perform()


import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.10/1/index.html"

with webdriver.Chrome() as driver:
    driver.get(url)

    # Находим элементы
    draganddrop = driver.find_element(By.CLASS_NAME, "draganddrop")
    draganddrop_end = driver.find_element(By.CLASS_NAME, "draganddrop_end")

    # Выполняем перетаскивание
    ActionChains(driver).drag_and_drop(draganddrop, draganddrop_end).perform()
    time.sleep(5)

############OFFSET

# action.move_by_offset(xoffset, yoffset) - используется для перемещения указателя мыши от текущего положения на определенное смещение по осям X и Y.

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.10/5/index.html"

with webdriver.Chrome() as driver:
    driver.get(url)
    slider = driver.find_element(By.ID, "volume")
    time.sleep(3)

    ActionChains(driver).click_and_hold(slider).move_by_offset(50, 0).release().perform()

    time.sleep(10)