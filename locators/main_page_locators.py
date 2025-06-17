from selenium.webdriver.common.by import By

class MainPageLocators:
    main_header = By.XPATH, '//div[contains(@class, "Home_Header__iJKdX")]'
    faq_section = By.XPATH, '//div[contains(@class, "Home_FAQ__3uVm4")]'
    faq_questions_items = {
        1: (By.XPATH, '//div[@id="accordion__heading-0"]'),
        2: (By.XPATH, '//div[@id="accordion__heading-1"]'),
        3: (By.XPATH, '//div[@id="accordion__heading-2"]'),
        4: (By.XPATH, '//div[@id="accordion__heading-3"]'),
        5: (By.XPATH, '//div[@id="accordion__heading-4"]'),
        6: (By.XPATH, '//div[@id="accordion__heading-5"]'),
        7: (By.XPATH, '//div[@id="accordion__heading-6"]'),
        8: (By.XPATH, '//div[@id="accordion__heading-7"]')
    }
    faq_answers_items = {
        1: (By.XPATH, '//div[@id="accordion__panel-0"]'),
        2: (By.XPATH, '//div[@id="accordion__panel-1"]'),
        3: (By.XPATH, '//div[@id="accordion__panel-2"]'),
        4: (By.XPATH, '//div[@id="accordion__panel-3"]'),
        5: (By.XPATH, '//div[@id="accordion__panel-4"]'),
        6: (By.XPATH, '//div[@id="accordion__panel-5"]'),
        7: (By.XPATH, '//div[@id="accordion__panel-6"]'),
        8: (By.XPATH, '//div[@id="accordion__panel-7"]')
    }

    order_button_in_main = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g Button_Middle__1CSJM")]')
    order_button_in_header = (By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[contains(@class, "Button_Button__ra12g")]')
    header_logo_scooter = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')
    header_logo_yandex = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')
    title_dzen = (By.TAG_NAME, 'title')
