from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def find_element(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(
                expected_conditions.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Элемент не найден: {locator[1]} за {time} секунд")

    def click_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def get_main_logo(self):
        return self.find_element(BasePageLocators.MAIN_LOGO)

    def get_ya_logo(self):
        return WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(BasePageLocators.YA_LOGO))
    
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    