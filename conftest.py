import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    driver.implicitly_wait(10)
    cookie_button = driver.find_element(By.CSS_SELECTOR, "#rcc-confirm-button")
    cookie_button.click()
    yield driver
    driver.quit()


