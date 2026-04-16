import pytest
import allure
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
    @allure.title("Заказ через верхнюю кнопку: {data[name]} {data[surname]}")
    def test_order_flow_top_button(self, driver, data):
        page = OrderPage(driver)
        page.click_order_button()
        page.fill_order_form(data)
        assert page.check_success_order()
        
    @pytest.mark.parametrize("data", ORDER_DATA)
    @allure.title("Заказ через нижнюю кнопку: {data[name]} {data[surname]}")
    def test_order_flow_bottom_button(self, driver, data):
        page = OrderPage(driver)
        page.click_bottom_order_button()
        page.fill_order_form(data)
        assert page.check_success_order()
        
    