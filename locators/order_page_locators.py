from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Кнопки заказа
    ORDER_TOP_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']") # Кнопка заказа сверху
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']") # Кнопка заказа снизу
    
    # Форма заказа
    NAME_FIELD = (By.XPATH, ".//input[@placeholder = '* Имя']") # Поле имени
    SURNAME_FIELD = (By.XPATH, ".//input[@placeholder = '* Фамилия']") # Поле фамилия
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']") # Поле адреса
    PHONE_FIELD = (By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']") # Поле телефона
    METRO_FIELD = (By.XPATH, ".//input[@placeholder = '* Станция метро']") # Поле станции метро
    METRO_FIELD_CLICK = (By.CSS_SELECTOR, 'button.Order_SelectOption__82bhS') # Кнопка выбора метро
    ORDER_NEXT_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Далее')]") # Кнопка Далее в форме
    DATE_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]') # Поле когда привезти самокат
    CALENDAR_CLICK = (By.CSS_SELECTOR,'div[aria-label="Choose пятница, 1-е мая 2026 г."]') # Выбор даты
    RENTAL_PERIOD_FIELD = (By.CSS_SELECTOR, 'div.Dropdown-placeholder') # Поле срока аренды
    CHOOSING_DATE = (By.XPATH,'//div[contains(@class, "Dropdown-option") and text() = "сутки"]') # выбор кол-ва дней аренды
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Middle__1CSJM:nth-child(2)") # Итоговая кнопка "заказать" в форме выбора срока аренды
    YES_BUTTON_ORDER = (By.XPATH, "//button[contains(@class, 'Button_Button') and . = 'Да']") # Кнопка "Да" подтверждения заказа
    
    # Сообщения
    SUCCESS_ORDER_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]") # сообщение об оформлении заказа

