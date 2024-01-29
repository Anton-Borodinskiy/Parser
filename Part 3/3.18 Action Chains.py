# Import
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# # Использование ActionChains для выполнения последовательности действий
#
# actions = ActionChains(driver) # Создаём экземпляр класса ActionChains
# actions.move_to_element(menu)  # Переместить курсор на элемент меню
# actions.click(submenu)         # Кликнуть по подменю
# actions.perform()              # Выполнить накопленные действия
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#START----------------------
# Инициализация драйвера
driver = webdriver.Chrome()

# Открыть веб-страницу (замените URL на ваш адрес)
driver.get("https://parsinger.ru/selenium/5.7/2/index.html")

# Найти элемент на странице с использованием локатора By
draggable = driver.find_element(By.ID, "draggable")

# Использование ActionChains для выполнения перетаскивания элемента
actions = ActionChains(driver)

# 1. Переместить блок влево на 100px
actions.drag_and_drop_by_offset(draggable, -100, 0).perform()
# 2. Переместить блок вниз на 100px
actions.drag_and_drop_by_offset(draggable, 0, 100).perform()

# 3. Переместить блок вправо на 100px
actions.drag_and_drop_by_offset(draggable, 100, 0).perform()

# 4. Переместить блок вверх на 100px
actions.drag_and_drop_by_offset(draggable, 0, -100).perform()

# Закрыть браузер после завершения
driver.quit()

#END###########################
# MORE EXAMPLES
# actions = ActionChains(driver) # Создаём экземпляр класса ActionChains
# element = driver.find_element(By.ID, "draggable") # Находим необходимый элемент/тег
#
#
#
# # Найти исходный и целевой элементы на странице с использованием локаторов By
# source = driver.find_element(By.ID, "source_element_id")
# target = driver.find_element(By.ID, "target_element_id")
#
# # Использование ActionChains для выполнения перетаскивания элемента
# actions = ActionChains(driver)
# actions.drag_and_drop(source, target).perform()

##################### METHODS
# action.perform(self) — Метод используется для выполнения всех сохраненных операций в экземпляре действия класса ActionChains. Запускает всю цепочку действий.
# action.click(element) — Кликает по элементу.
# action.click_and_hold(element) — Удерживает левую кнопку мыши на элементе.
# action.context_click(element) — Используется для выполнения контекстного щелчка (щелчка правой кнопкой мыши) по элементу.
# action.drag_and_drop(source, target) — Удерживает левую кнопку мыши на исходном элементе, затем перемещается к целевому элементу и отпускает кнопку мыши.
# # action.release(self, on_element=None)  — Метод release используется для отпускания удерживаемой кнопки мыши на элементе.
# action.drag_and_drop_by_offset(source, xoffset, yoffset)  — Удерживает левую кнопку мыши на исходном элементе, затем перемещается к заданному смещению и отпускает кнопку мыши.

# Использование ActionChains для выполнения перетаскивания элемента на заданное смещение
# actions = ActionChains(driver)
# actions.drag_and_drop_by_offset(source_element, 50, 100).perform()  # Перемещает элемент на 50px вправо и 100px вниз


#HOLD KEYS
# Использование ActionChains для удержания клавиш
# actions = ActionChains(driver)
# actions.key_down(Keys.CONTROL, element) \
#        .key_down(Keys.ALT) \
#        .key_down(Keys.SHIFT) \
#        .key_down('T') \
#        .perform()
# # После выполнения необходимых действий, не забудьте отпустить клавиши
# actions.key_up(Keys.CONTROL) \
#        .key_up(Keys.ALT) \
#        .key_up(Keys.SHIFT) \
#        .key_up('T') \
#        .perform()

# # Использование move_by_offset для перемещения курсора мыши на 50px вправо и 100px вниз
# actions.move_by_offset(50, 100).perform()


# # Найти элемент на странице, к которому вы хотите переместить курсор
# menu_element = driver.find_element(By.ID, "menu_item")
#
# # Использование ActionChains для перемещения курсора к элементу
# actions = ActionChains(driver)
# actions.move_to_element(menu_element).perform()

# # Переместить курсор мыши на 50px вправо и 30px вниз от верхнего левого угла элемента element_to_hover
# actions.move_to_element_with_offset(element_to_hover, 50, 30).perform()

# action.pause(seconds) — Метод паузы используется для приостановки всех входящих данных на указанное время в секундах. Метод паузы очень важен и полезен в случае выполнения какой-либо команды, для загрузки которой требуется какой-либо JavaScript, или в подобной ситуации, когда между двумя операциями есть временной промежуток.

# action.send_keys(Keys.DOWN) — метод используется для отправки ключей текущему элементу в фокусе;
#
# # Найти элемент на странице с использованием локатора By
# input_element = driver.find_element(By.ID, "inputField")
#
# # Использование ActionChains для отправки нажатия клавиш элементу
# actions = ActionChains(driver)
# actions.send_keys_to_element(input_element, "Hello", Keys.SPACE, "World!").perform()

# action.scroll(x, y, delta_x, delta_y, duration, origin=element)  —  Выполняет скроллинг на элементе, где установлен курсор. Очень полезный скроллинг, позволяет прицельно скролить окна маленьких размеров;
# action.reset_actions(self) — Метод очищает действия, которые уже сохранены локально и в ActionChains. Это один из наиболее часто используемых методов, так как после какой-либо операции необходимо сбросить экземпляр ActionChains для выполнения следующей операции.


# # Использование ActionChains для прокрутки на заданное количество
# actions = ActionChains(driver)
# actions.scroll_by_amount(delta_x=50, delta_y=100).perform()  # Прокрутка на 50 пикселей вправо и 100 пикселей вниз


# # Найти элемент на странице с использованием локатора By
# element_to_scroll = driver.find_element(By.ID, "someElement")
#
# # Использование ActionChains для выполнения прокрутки относительно элемента
# actions = ActionChains(driver)
# actions.scroll_from_origin(element_to_scroll 0, 100).perform()  # Прокрутка вниз на 100 пикселей относительно элемента


# # Найти элемент на странице
# element = driver.find_element(By.ID, "someElement")
#
# # Использование ActionChains для прокрутки к элементу
# actions = ActionChains(driver)
# actions.scroll_to_element(element).perform()