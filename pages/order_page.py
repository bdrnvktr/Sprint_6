import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class OrderPage(BasePage):
    @allure.step("Клик по верхней кнопке заказа")
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_TOP_BUTTON)

    @allure.step("Клик по нижней кнопке заказа")
    def click_bottom_order_button(self):
        element = WebDriverWait(self.driver, 15).until(
        expected_conditions.element_to_be_clickable(OrderPageLocators.BOTTOM_ORDER_BUTTON))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Заполнение формы заказа данными: {data}")
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

    @allure.step("Проверка успешного создания заказа")
    def check_success_order(self):  
        elements = self.driver.find_elements(*OrderPageLocators.SUCCESS_ORDER_MESSAGE)
        return len(elements) > 0 and elements[0].is_displayed()

    