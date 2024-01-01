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


class RadioButtonPageLocators:
    RESULT_FIELD = (By.XPATH, '//span[@class="text-success"]')


class WebTablesLocators:
    # add person information
    ADD_BTN = (By.ID, 'addNewRecordButton')
    FIRST_NAME_FIELD = (By.ID, 'firstName')
    LAST_NAME_FIELD = (By.ID, 'lastName')
    EMAIL_FIELD = (By.ID, 'userEmail')
    AGE_FIELD = (By.ID, "age")
    SALARY_FIELD = (By.ID, 'salary')
    DEPARTMENT_FIELD = (By.ID, 'department')
    SUBMIT_BTN = (By.ID, 'submit')

    # table
    FULL_PERSONS_LIST = (By.XPATH, '//div[@class="rt-tr-group"]')

