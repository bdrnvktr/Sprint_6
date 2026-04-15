import pytest
import allure
from pages.order_page import OrderPage

class TestLogo:
    @allure.title("Проверка навигации по логотипам после нажатия верхней кнопки «Заказать»")
    def test_logo_navigation_after_top_order_button(self, driver):
        page = OrderPage(driver)
        # Шаг 1. Нажимаем верхнюю кнопку «Заказать»
        page.click_order_button()
        # Шаг 2. Нажимаем логотип Самоката и проверяем переход на главную страницу
        assert page.click_and_check_scooter_logo(), "Переход по логотипу Самоката не удался — не произошёл переход на главную страницу"
        # Шаг 3. Возвращаемся на страницу заказа: снова нажимаем верхнюю кнопку «Заказать»
        page.click_order_button()
        # Шаг 4. Нажимаем логотип Яндекса и проверяем открытие Дзена в новой вкладке
        assert page.click_and_check_ya_logo(), "Открытие Дзена по логотипу Яндекса не удалось — новая вкладка не открылась или URL неверный"