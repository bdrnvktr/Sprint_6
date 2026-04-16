import allure
from locators.faq_page_locators import FaqPageLocators
from pages.base_page import BasePage

class FaqPage(BasePage):
    @allure.step("Клик по вопросу FAQ №{question_number}")
    def click_faq_question(self, question_number):
        locator = getattr(FaqPageLocators, f"FAQ_QUESTION_{question_number}")
        self.click_element(locator)

    @allure.step("Получение ответа на вопрос FAQ №{answer_number}")
    def get_faq_answer(self, answer_number):
        locator = getattr(FaqPageLocators, f"FAQ_ANSWER_{answer_number}")
        return self.find_element(locator)

