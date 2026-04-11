from selenium.webdriver.common.by import By


class FaqPageLocators:
    # Вопросы — ищем по тексту внутри элемента
    FAQ_QUESTION_1 = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton' and contains(text(), 'Сколько это стоит? И как оплатить?')]")
    FAQ_QUESTION_2 = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton' and contains(text(), 'Хочу сразу несколько самокатов! Так можно?')]")
    FAQ_QUESTION_3 = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton' and contains(text(), 'Как рассчитывается время аренды?')]")
    FAQ_QUESTION_4 = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton' and contains(text(), 'Можно ли заказать самокат прямо на сегодня?')]")
    FAQ_QUESTION_5 = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton' and contains(text(), 'Можно ли продлить заказ или вернуть самокат раньше?')]")
    FAQ_QUESTION_6 = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton' and contains(text(), 'Вы привозите зарядку вместе с самокатом?')]")
    FAQ_QUESTION_7 = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton' and contains(text(), 'Можно ли отменить заказ?')]")
    FAQ_QUESTION_8 = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton' and contains(text(), 'Я жизу за МКАДом, привезёте?')]")

    # Ответы
    FAQ_ANSWER_1 = (By.XPATH, "//div[@class='accordion__panel' and @aria-labelledby='accordion__heading-0']")
    FAQ_ANSWER_2 = (By.XPATH, "//div[@class='accordion__panel' and @aria-labelledby='accordion__heading-1']")
    FAQ_ANSWER_3 = (By.XPATH, "//div[@class='accordion__panel' and @aria-labelledby='accordion__heading-2']")
    FAQ_ANSWER_4 = (By.XPATH, "//div[@class='accordion__panel' and @aria-labelledby='accordion__heading-3']")
    FAQ_ANSWER_5 = (By.XPATH, "//div[@class='accordion__panel' and @aria-labelledby='accordion__heading-4']")
    FAQ_ANSWER_6 = (By.XPATH, "//div[@class='accordion__panel' and @aria-labelledby='accordion__heading-5']")
    FAQ_ANSWER_7 = (By.XPATH, "//div[@class='accordion__panel' and @aria-labelledby='accordion__heading-6']")
    FAQ_ANSWER_8 = (By.XPATH, "//div[@class='accordion__panel' and @aria-labelledby='accordion__heading-7']")