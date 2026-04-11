import pytest
from pages.order_page import OrderPage


ORDER_DATA = [
    {
        'name': 'Иван',
        'surname': 'Иванов',
        'address': 'Ленина, 1',
        'phone': '+79991234567',
        'metro': 'Бульвар Рокоссовского'
    },
    {
        'name': 'Петр',
        'surname': 'Петров',
        'address': 'Невский проспект',
        'phone': '+79997654321',
        'metro': 'Черкизовская'
    }
]

class TestOrderFlow:
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_order_flow_top_button(self, driver, data):
        page = OrderPage(driver)
        page.click_order_button()
        page.fill_order_form(data)
        assert page.check_success_order()
        
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_order_flow_bottom_button(self, driver, data):
        page = OrderPage(driver)
        page.click_bottom_order_button()
        page.fill_order_form(data)
        assert page.check_success_order()
        
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