from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.ID, 'userName')
    EMAIL = (By.ID, 'userEmail')
    CURRENT_ADDRESS = (By.ID, 'currentAddress')
    PERMANENT_ADDRESS = (By.ID, 'permanentAddress')
    SUBMIT_BTN = (By.XPATH, '//button[@id="submit"]')

    CREATED_NAME_FIELD = (By.XPATH, '//p[@id="name"]')
    CREATED_EMAIL_FIELD = (By.XPATH, '//p[@id="email"]')
    CREATED_CURRENT_ADDRESS_FIELD = (By.XPATH, '//p[@id="currentAddress"]')
    CREATED_PERMANENT_ADDRESS_FIELD = (By.XPATH, '//p[@id="permanentAddress"]')


class CheckBoxPageLocators:
    EXPAND_ALL_BTN = (By.XPATH, '//button[@title="Expand all"]')
    ITEM_LIST = (By.XPATH, "//span[@class='rct-title']")
    DOCUMENTS_CHECKBOX = (By.XPATH, '//span[text()="Documents"]')
    RESULT = (By.ID, 'result')
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')
