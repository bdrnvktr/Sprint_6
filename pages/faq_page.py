from locators.faq_page_locators import FaqPageLocators
from pages.base_page import BasePage


class FaqPage(BasePage):
    # Методы для работы с вопросами FAQ

    # Кликает по первому вопросу FAQ
    def click_faq_question_1(self):
        self.click_element(FaqPageLocators.FAQ_QUESTION_1)

    # Кликает по второму вопросу FAQ
    def click_faq_question_2(self):
        self.click_element(FaqPageLocators.FAQ_QUESTION_2)
        
    # Кликает по третьему вопросу FAQ
    def click_faq_question_3(self):
        self.click_element(FaqPageLocators.FAQ_QUESTION_3)
        
    # Кликает по четвертому вопросу FAQ
    def click_faq_question_4(self):
        self.click_element(FaqPageLocators.FAQ_QUESTION_4)
        
    # Кликает по пятому вопросу FAQ
    def click_faq_question_5(self):
        self.click_element(FaqPageLocators.FAQ_QUESTION_5)
        
    # Кликает по шестому вопросу FAQ
    def click_faq_question_6(self):
        self.click_element(FaqPageLocators.FAQ_QUESTION_6)
        
    # Кликает по седьмому вопросу FAQ
    def click_faq_question_7(self):
        self.click_element(FaqPageLocators.FAQ_QUESTION_7)
        
    # Кликает по восьмому вопросу FAQ
    def click_faq_question_8(self):
        self.click_element(FaqPageLocators.FAQ_QUESTION_8)

    # Методы для получения ответов на вопросы FAQ
    
    # Возвращает текст ответа на первый вопрос
    def get_faq_answer_1(self):
        return self.find_element(FaqPageLocators.FAQ_ANSWER_1)
        
    # Возвращает текст ответа на второй вопрос
    def get_faq_answer_2(self):
        return self.find_element(FaqPageLocators.FAQ_ANSWER_2)
        
    # Возвращает текст ответа на третий вопрос
    def get_faq_answer_3(self):
        return self.find_element(FaqPageLocators.FAQ_ANSWER_3)
        
    # Возвращает текст ответа на четвертый вопрос
    def get_faq_answer_4(self):
        return self.find_element(FaqPageLocators.FAQ_ANSWER_4)
        
    # Возвращает текст ответа на пятый вопрос
    def get_faq_answer_5(self):
        return self.find_element(FaqPageLocators.FAQ_ANSWER_5)
        
    # Возвращает текст ответа на шестой вопрос
    def get_faq_answer_6(self):
        return self.find_element(FaqPageLocators.FAQ_ANSWER_6)
        
    # Возвращает текст ответа на седьмой вопрос
    def get_faq_answer_7(self):
        return self.find_element(FaqPageLocators.FAQ_ANSWER_7)
        
    # Возвращает текст ответа на восьмой вопрос
    def get_faq_answer_8(self):
        return self.find_element(FaqPageLocators.FAQ_ANSWER_8)
    
    

