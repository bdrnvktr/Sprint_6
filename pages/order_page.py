from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class OrderPage(BasePage):
    # Метод для клика по верхней кнопке заказа
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_TOP_BUTTON)

    # Метод для клика по нижней кнопке заказа
    def click_bottom_order_button(self):
        element = WebDriverWait(self.driver, 15).until(
        expected_conditions.element_to_be_clickable(OrderPageLocators.BOTTOM_ORDER_BUTTON))
        self.driver.execute_script("arguments[0].click();", element)
    # Метод для оформления заказа
    def fill_order_form(self, data):
        # Заполняем поля формы
        self.find_element(OrderPageLocators.NAME_FIELD).send_keys(data['name'])
        self.find_element(OrderPageLocators.SURNAME_FIELD).send_keys(data['surname'])
        self.find_element(OrderPageLocators.ADDRESS_FIELD).send_keys(data['address'])
        self.find_element(OrderPageLocators.PHONE_FIELD).send_keys(data['phone'])
        self.find_element(OrderPageLocators.METRO_FIELD).send_keys(data['metro'])
        self.click_element(OrderPageLocators.METRO_FIELD_CLICK)
        # Нажимаем кнопку "Далее"
        self.click_element(OrderPageLocators.ORDER_NEXT_BUTTON)
        # Выбираем период аренды
        self.click_element(OrderPageLocators.DATE_FIELD)
        self.click_element(OrderPageLocators.CALENDAR_CLICK)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_element(OrderPageLocators.CHOOSING_DATE)
        # Подтверждаем заказ
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.YES_BUTTON_ORDER)

    # Метод для проверки успешного создания заказа
    def check_success_order(self):
        try:
            self.find_element(OrderPageLocators.SUCCESS_ORDER_MESSAGE)
            return True
        except TimeoutException:
            return False

    # Метод для проверки возврата на гравную страницу по клику
    def click_and_check_scooter_logo(self):
        current_url = self.driver.current_url
        self.get_main_logo().click()
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url != current_url)
        return "qa-scooter.praktikum-services.ru" in self.driver.current_url

    # Метод для проверки открытия страницы Дзена по клику на логотип Яндекса
    def click_and_check_ya_logo(self):
        print(f"Текущий URL перед кликом: {self.driver.current_url}")
        original_window = self.driver.current_window_handle
    # Ждём, пока элемент станет кликабельным, и получаем его
        ya_logo = WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(BasePageLocators.YA_LOGO))
        print(f"Найден элемент: {ya_logo.get_attribute('outerHTML')}")
    # Получаем текущий href и исправляем протокол, если нужно
        href = ya_logo.get_attribute("href")
        if href and href.startswith("//"):
            href = "https:" + href
            print(f"Исправленный href: {href}")
    # Пытаемся открыть ссылку тремя способами (по приоритету)
        try:
        # Способ 1: обычный клик
            ya_logo.click()
        except Exception:
            try:
            # Способ 2: клик через JavaScript
                self.driver.execute_script("arguments[0].click();", ya_logo)
            except Exception:
                try:
                # Способ 3: принудительное открытие в новой вкладке через Ctrl+клик
                    from selenium.webdriver.common.keys import Keys
                    from selenium.webdriver import ActionChains
                    actions = ActionChains(self.driver)
                    actions.key_down(Keys.CONTROL).click(ya_logo).key_up(Keys.CONTROL).perform()
                except Exception as e:
                    print(f"Все способы клика провалились: {e}")
                    return False
    # Ждём появления новой вкладки (увеличенный таймаут до 30 секунд)
        WebDriverWait(self.driver, 30).until(lambda driver: len(driver.window_handles) > 1)
    # Получаем список всех открытых вкладок
        all_windows = self.driver.window_handles
        new_window = None
    # Ищем новую вкладку (ту, что не является оригинальной)
        for window in all_windows:
            if window != original_window:
                new_window = window
                break
    # Если новая вкладка не открылась, возвращаем False
        if not new_window:
            print("Ошибка: новая вкладка не открылась после 30 секунд ожидания!")
            return False
        try:
        # Переключаемся на новую вкладку
            self.driver.switch_to.window(new_window)
        # Ждём, пока URL изменится с about:blank (возможна задержка загрузки)
            WebDriverWait(self.driver, 20).until(lambda driver: driver.current_url != "about:blank")
        # Ждём полной загрузки страницы в новой вкладке
            WebDriverWait(self.driver, 25).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        # Получаем текущий URL и выводим его для отладки
            current_url = self.driver.current_url
            print(f"Текущий URL новой вкладки: {current_url}")
        # Проверяем, содержит ли URL 'dzen.ru' (универсальная проверка)
            result = "dzen.ru" in current_url
        # Закрываем новую вкладку
            self.driver.close()
        # Возвращаемся к исходной вкладке
            self.driver.switch_to.window(original_window)
            return result
        except Exception as e:
        # В случае любой ошибки выводим сообщение и возвращаем False
            print(f"Ошибка при работе с вкладкой: {e}")
            try:
            # Пытаемся вернуться к исходной вкладке, если возможно
                self.driver.switch_to.window(original_window)
            except:
                pass
            return False