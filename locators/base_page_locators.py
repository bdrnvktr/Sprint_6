from selenium.webdriver.common.by import By

class BasePageLocators:
    # Основные элементы главной страницы
    MAIN_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')  # Логотип Самоката
    YA_LOGO = (By.CSS_SELECTOR, 'a.Header_LogoYandex__3TSOI[href*="yandex.ru"]') # Логотип Яндекса 
    COOKIE_BUTTON = (By.CSS_SELECTOR, '#rcc-confirm-button') # Кнопка подтверждения куки