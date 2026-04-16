import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента по локатору")    
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator))

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    @allure.step("Получение логотипа Самоката")
    def get_main_logo(self):
        return self.find_element(BasePageLocators.MAIN_LOGO)

    @allure.step("Ожидание видимости логотипа Яндекса")
    def get_ya_logo(self):
        return WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(BasePageLocators.YA_LOGO))
    
    @allure.step("Прокрутка страницы до низа")
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Клик по логотипу Самоката и проверка перехода на главную страницу")
    def click_and_check_scooter_logo(self):
        current_url = self.driver.current_url
        self.get_main_logo().click()
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url != current_url)
        return "qa-scooter.praktikum-services.ru" in self.driver.current_url

    @allure.step("Клик по логотипу Яндекса и проверка открытия Дзена в новой вкладке")
    def click_and_check_ya_logo(self):
        original_window = self.driver.current_window_handle
        self.click_element(BasePageLocators.YA_LOGO)
        WebDriverWait(self.driver, 30).until(lambda driver: len(driver.window_handles) > 1)
        all_windows = self.driver.window_handles
        new_window = all_windows[1]
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 20).until(lambda driver: driver.current_url != "about:blank")
        WebDriverWait(self.driver, 25).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        current_url = self.driver.current_url
        assert "dzen.ru" in current_url
        self.driver.close()
        self.driver.switch_to.window(original_window)
        return True