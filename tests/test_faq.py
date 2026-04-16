import pytest
import allure
from pages.faq_page import FaqPage


@pytest.fixture(autouse=True)
def scroll_before_each_test(driver):
    page = FaqPage(driver)
    page.scroll_to_bottom()

class TestFaqPage:
    EXPECTED_ANSWERS = {
    1: "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
    2: "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
    3: "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
    4: "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
    5: "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
    6: "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
    7: "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
    8: "Да, обязательно. Всем самокатов! И Москве, и Московской области."
}

    @pytest.mark.parametrize("question_number", range(1, 9))
    @allure.title("FAQ: проверка вопроса №{question_number}")
    def test_faq_questions(self, driver, question_number):
        page = FaqPage(driver)
        page.click_faq_question(question_number)
        answer_element = page.get_faq_answer(question_number)
        actual_answer_text = answer_element.text.strip()
        expected_answer = self.EXPECTED_ANSWERS[question_number]
        assert expected_answer in actual_answer_text