# webdriver.back() - С помощью этого метода вы можете вернуться на предыдущую страницу, как если бы нажали стрелочку "назад" в браузере.
# webdriver.forward() - Аналогично предыдущему, но перемещает вперёд по истории браузера.
# webdriver.refresh() -  Этот метод обновляет текущую страницу, как если бы вы нажали кнопку обновления в браузере.
# webdriver.get_screenshot_as_file("../file_name.jpg") - Сохраняет скриншот страницы в файл по указанному пути. Возвращает True если всё прошло успешно, и False при ошибках ввода-вывода.
# webdriver.save_screenshot("file_name.jpg") - Сохраняет скриншот в папке с проектом.
# webdriver.get_screenshot_as_png() - Возвращает скриншот в виде двоичных данных (binary data), которые можно передать или сохранить в файл в конструкторе with/as;
# webdriver.get_screenshot_as_base64() - Возвращает скриншот в виде строки в кодировке Base64. Удобно для встроенных изображений в HTML.

# webdriver.get("http://example_url.ru")
# webdriver.quit()
# webdriver.close()
# webdriver.execute_script("script_code") - Выполняет JavaScript код на текущей странице.
# webdriver.execute_async_script("script_code" , *args ) - Асинхронно выполняет JavaScript код. Удобно для работы с AJAX и промисами.

# webdriver.set_page_load_timeout() - Устанавливает таймаут на загрузку страницы. Выбрасывает исключение, если время вышло.

# webdriver.find_element(By.ID, 'example_id') - Возвращает первый найденный элемент по заданному локатору.
# webdriver.find_elements(By.ID, 'example_id') - Возвращает список всех элементов, соответствующих локатору.

# webdriver.get_window_position() - Возвращает словарь с текущей позицией окна браузера ({'x': 10, 'y': 50}).
# webdriver.maximize_window() - Разворачивает окно на весь экран.
# webdriver.minimize_window() - Сворачивает окно.
# webdriver.fullscreen_window()  - Переводит окно в полноэкранный режим, как при нажатии F11.
#
# webdriver.get_window_size() - Возвращает размер окна в виде словаря ({'width': 945, 'height': 1020}).
#
# webdriver.set_window_size(800,600) - Устанавливает новый размер окна.



# webdriver.get_cookies()  - Возвращает список всех cookies.
#
# webdriver.get_cookie(name_cookie) - Возвращает конкретную cookie по имени.
#
# webdriver.add_cookie(cookie_dict) - Добавляет новую cookie к вашему текущему сеансу;
#
# webdriver.delete_cookie(name_cookie) - Удаляет cookie по имени.
#
# webdriver.delete_all_cookies() - удаляет все файлы cookie в рамках текущего сеанса;

# webdriver.implicitly_wait(10) - Устанавливает неявное ожидание на поиск элементов или выполнение команд.
#
# webdriver.WebDriverWait(driver, timeout).until(condition)




# element.click() - Симулирует клик по элементу.
#
# element.send_keys("text") - Вводит текст в текстовое поле. Очень полезно для автоматизации ввода данных.
#
# element.clear() - Очищает текстовое поле.
#
# element.is_displayed() - Проверяет, отображается ли элемент на странице.
#
# element.is_enabled() - Проверяет, доступен ли элемент для взаимодействия (например, не заблокирован).
#
# element.is_selected() - Проверяет, выбран ли элемент (актуально для радиокнопок и чекбоксов).
#
# element.get_attribute("attribute") - Возвращает значение указанного атрибута элемента.
#
# element.text - Возвращает текст элемента.
#
# element.submit() - Отправляет форму, в которой находится элемент.


# webdriver.switch_to.frame("frame_name") - Переключает фокус на указанный фрейм.
#
# webdriver.switch_to.default_content() - Возвращает фокус на основное содержимое страницы, выходя из фрейма.


# webdriver.switch_to.alert - Переключает фокус на всплывающее окно JavaScript.