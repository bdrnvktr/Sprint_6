import pytest
import allure
from pages.faq_page import FaqPage


@pytest.fixture(autouse=True)
def scroll_before_each_test(driver):
    page = FaqPage(driver)
    page.scroll_to_bottom()

class TestFaqPage:
    @pytest.mark.parametrize("question_number", range(1, 9))
    @allure.title("FAQ: проверка вопроса №{question_number}")
    def test_faq_questions(self, driver, question_number):
        page = FaqPage(driver)
        page.click_faq_question(question_number)
        answer_element = page.get_faq_answer(question_number)
        assert answer_element.is_displayed()