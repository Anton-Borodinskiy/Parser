# WebDriverWait(browser, poll_frequency=0.5, timeout=10).until(EC.text_to_be_present_in_element((locator)))

# EC.text_to_be_present_in_element(locator, text_)— Это ожидаемое условие, которое проверяет, содержит ли текст элемента, определенного локатором, заданное подстроковое значение.
#
# #Определяем локатор и ожидаемый текст
# locator = (By.ID, 'message')
# expected_text = "Загрузка завершена"
#
# # Используем явное ожидание, чтобы убедиться, что элемент содержит ожидаемый текст
# WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(locator, expected_text))


# EC.text_to_be_present_in_element_value(locator, text_)— Это ожидаемое условие в Selenium, которое проверяет наличие определенного текста в значении атрибута value элемента, указанного локатором.
#
# # Определяем локатор и ожидаемый текст
# locator = (By.ID, 'search_field')
# expected_text = "Query123"
#
# # Используем явное ожидание, чтобы проверить наличие текста в атрибуте value элемента
# WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value(locator, expected_text))


# # EC.text_to_be_present_in_element_attribute(locator, attribute_, text_) —это ожидаемое условие, которое проверяет, содержится ли указанный текст в определенном атрибуте элемента, определенного локатором.
#
# # Определяем локатор, атрибут и ожидаемый текст
# locator = (By.ID, 'image_id')
# attribute_name = "alt"
# expected_text = "Descriptive Image Text"
#
# # Используем явное ожидание, чтобы удостовериться, что атрибут содержит нужный текст
# WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_attribute(locator, attribute_name, expected_text))

# EC.element_attribute_to_include(locator, attribute_)—это ожидаемое условие, которое проверяет, содержит ли атрибут элемента, определенного локатором, заданное значение.
# # # Определяем локатор и атрибут с ожидаемой подстрокой
# # locator = (By.ID, 'image_id')
# # attribute_info = ("src", "thumbnail")
# #
# # # Используем явное ожидание, чтобы удостовериться, что атрибут элемента содержит ожидаемую подстроку
# # WebDriverWait(driver, 10).until(EC.element_attribute_to_include(locator, attribute_info))


#WAITINGS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# EC.frame_to_be_available_and_switch_to_it(locator)— Это ожидаемое условие, которое проверяет доступность iframe на веб-странице и автоматически переключается на него.
locator = (By.ID, 'iframe_id')
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(locator))

# EC.invisibility_of_element_located(locator)— Это условие проверяет, что элемент, указанный локатором, больше не видим на веб-странице.

# EC.invisibility_of_element(element)
# Предположим, что element — это элемент всплывающего окна, который вы нашли ранее
element = driver.find_element(By.ID, 'popup')

# Теперь вы хотите дождаться, пока всплывающее окно исчезнет
WebDriverWait(driver, 10).until(EC.invisibility_of_element(element))


# EC.element_to_be_clickable(element)— Это условие, предназначено для ожидания, пока элемент на веб-странице не станет видимым и доступным для клика.
# Определение локатора для кнопки
button_locator = (By.ID, 'submit_button')

# Ожидание, пока кнопка не станет доступна для клика
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_locator))

# Теперь можно кликнуть по кнопке
button.click()

# EC.staleness_of(element)  Это ожидаемое условие, которое проверяет, стал ли element устаревшим, то есть исчез ли он с DOM-структуры страницы или был ли он перезагружен.
# Находим элемент
element = driver.find_element(By.ID, 'some_element')


# Выполняем действие, которое приведет к обновлению элемента (например, клик по кнопке)
driver.find_element(By.ID, 'update_button').click()

# Ожидаем, пока элемент станет устаревшим
WebDriverWait(driver, 10).until(EC.staleness_of(element))

# EC.element_to_be_selected(element) Это ожидаемое условие в Selenium, которое проверяет, выбран ли предоставленный элемент на веб-странице.
# Находим элемент (чекбокс) на странице
element = driver.find_element(By.ID, "my_checkbox")

# Используем явное ожидание, чтобы убедиться, что чекбокс выбран
WebDriverWait(driver, 10).until(EC.element_to_be_selected(element))

# EC.element_located_to_be_selected(locator) Это ожидаемое условие проверяет, выбран ли элемент, определенный по локатору. Элемент может быть чекбоксом, радиокнопкой или опцией в выпадающем списке.
# Определение локатора для чекбокса
checkbox_locator = (By.ID, 'accept_terms_checkbox')

# Ожидание, пока чекбокс не станет выбранным
WebDriverWait(driver, 10).until(EC.element_located_to_be_selected(checkbox_locator))

# EC.element_selection_state_to_be(element, is_selected) Это ожидаемое условие, которое проверяет, соответствует ли состояние выбора (выделения) элемента ожидаемому значению.
# Предположим, у нас есть чекбокс с ID "my_checkbox"
element = driver.find_element(By.ID, 'my_checkbox')

# Мы хотим удостовериться, что чекбокс отмечен
WebDriverWait(driver, 10).until(EC.element_selection_state_to_be(element, True))


# EC.element_located_selection_state_to_be(locator, is_selected) Это ожидаемое условие, которое проверяет, находится ли элемент, определенный локатором, в определенном состоянии выбора (выбран или не выбран).
locator = (By.ID, 'my_checkbox')
expected_state = True  # Ожидаем, что чекбокс будет отмечен

# Ожидаем, пока чекбокс не окажется в ожидаемом состоянии
WebDriverWait(driver, 10).until(EC.element_located_selection_state_to_be(locator, True))

# EC.number_of_windows_to_be(num_windows)  Условие ожидания, которое проверяет, равно ли текущее количество открытых окон в браузере заданному числу.
# Предполагаем, что изначально открыто одно окно
num_windows_before = len(driver.window_handles)

# Выполняем действие, которое должно открыть новое окно
driver.find_element(By.ID, 'some_link').click()

# Ожидаем, пока не откроется новое окно
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(num_windows_before + 1))

# Теперь можно безопасно переключиться на новое окно и продолжить тест
new_window_handle = [handle for handle in driver.window_handles if handle != driver.current_window_handle][0]
driver.switch_to.window(new_window_handle)


# EC.new_window_is_opened(current_handles) Это ожидаемое условие, которое проверяет, было ли открыто новое окно или вкладка браузера.
# Получаем список текущих открытых окон/вкладок
current_handles = driver.window_handles

# Выполняем действие, которое должно открыть новое окно/вкладку
driver.find_element(By.ID, 'open_new_window_button').click()

# Ждем открытия нового окна/вкладки
WebDriverWait(driver, 10).until(EC.new_window_is_opened(current_handles))

# Получаем новый список окон/вкладок
new_handles = driver.window_handles

# Находим идентификатор нового окна/вкладки
new_window = [handle for handle in new_handles if handle not in current_handles][0]

# Переключаемся на новое окно/вкладку
driver.switch_to.window(new_window)

# EC.alert_is_present()— Является ожидаемым условием и предназначена для проверки наличия всплывающего окна предупреждения (alert) на веб-странице.
# Используем явное ожидание для проверки наличия всплывающего окна предупреждения
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

# После этого можно взаимодействовать с всплывающим окном
text = alert.text
alert.accept()