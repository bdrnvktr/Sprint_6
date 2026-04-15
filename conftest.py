import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators
from constants import BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    driver.implicitly_wait(10)
    cookie_button = driver.find_element(*BasePageLocators.COOKIE_BUTTON)
    cookie_button.click()
    yield driver
    driver.quit()


