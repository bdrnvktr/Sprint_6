import pytest
from pages.faq_page import FaqPage


@pytest.fixture(autouse=True)
def scroll_before_each_test(driver):
    page = FaqPage(driver)
    page.scroll_to_bottom()
    
class TestFaqPage:
    def test_faq_question_1(self, driver):
        page = FaqPage(driver)
        page.click_faq_question_1()
        assert page.get_faq_answer_1().is_displayed()

    def test_faq_question_2(self, driver):
        page = FaqPage(driver)
        page.click_faq_question_2()
        assert page.get_faq_answer_2().is_displayed()

    def test_faq_question_3(self, driver):
        page = FaqPage(driver)
        page.click_faq_question_3()
        assert page.get_faq_answer_3().is_displayed()

    def test_faq_question_4(self, driver):
        page = FaqPage(driver)
        page.click_faq_question_4()
        assert page.get_faq_answer_4().is_displayed()

    def test_faq_question_5(self, driver):
        page = FaqPage(driver)
        page.click_faq_question_5()
        assert page.get_faq_answer_5().is_displayed()

    def test_faq_question_6(self, driver):
        page = FaqPage(driver)
        page.click_faq_question_6()
        assert page.get_faq_answer_6().is_displayed()

    def test_faq_question_7(self, driver):
        page = FaqPage(driver)
        page.click_faq_question_7()
        assert page.get_faq_answer_7().is_displayed()

    def test_faq_question_8(self, driver):
        page = FaqPage(driver)
        page.click_faq_question_8()
        assert page.get_faq_answer_8().is_displayed()

        