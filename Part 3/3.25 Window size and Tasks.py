import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#TASK3
window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
with webdriver.Chrome() as browser:
    # Открываем указанный URL в браузере.
    browser.get('https://parsinger.ru/window_size/2/index.html')
    for x in window_size_x:
        for y in window_size_y:
            browser.set_window_size(x+16, y+138)
            time.sleep(0.3)
            if browser.find_element(By.ID, 'result').text.isdigit():
                print(browser.get_window_size())

#TASK2
window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
with webdriver.Chrome() as browser:
    # Открываем указанный URL в браузере.
    browser.get('https://parsinger.ru/window_size/2/index.html')
    for x in window_size_x:
        for y in window_size_y:
            browser.set_window_size(x+16, y+138)
            if len(browser.find_element(By.ID, 'result').text) > 0:
                print(browser.find_element(By.ID, 'result').text)


#TASK1
with webdriver.Chrome() as browser:
    # Открываем указанный URL в браузере.
    browser.get('https://parsinger.ru/window_size/1/')
    browser.set_window_size(571, 693)
    time.sleep(5)

    # with webdriver.Chrome() as browser:
    #     browser.get('http://parsinger.ru/window_size/1/index.html')
    #     browser.set_window_size(555 + 16, 555 + 133)
    #     print(browser.find_element(By.ID, 'result').text)

# 16px занимают боковые границы браузера: левая и правая.
# 138px занимает верхняя панель управления браузера и нижняя граница.
with webdriver.Chrome() as browser:
    # Открываем указанный URL в браузере.
    browser.get('http://parsinger.ru/window_size/1/')
    print(browser.get_window_size().get('height'))
    # Устанавливаем размер окна браузера на 1200 пикселей в ширину и 720 пикселей в высоту.
    browser.set_window_size(1200, 720)

    # Получаем текущий размер окна браузера в виде словаря, где 'height' - высота окна,
    # 'width' - ширина окна. И затем печатаем значение высоты окна.
    print(browser.get_window_size().get('height'))

    # Аналогично печатаем значение ширины окна.
    print(browser.get_window_size().get('width'))
    time.sleep(5)

# После завершения выполнения кода в блоке 'with', браузер автоматически закрывается.