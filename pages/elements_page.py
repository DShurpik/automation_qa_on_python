from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.elements_page_locators import TextBoxPageLocators
from basePages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_full_name_fields(self, username):
        self.element_is_visible(self.locators.FULL_NAME).send_keys(username)
        return self

    def fill_email_fields(self, email):
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        return self

    def fill_current_address_fields(self, current_address):
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        return self

    def fill_permanent_address_fields(self, permanent_address):
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        return self

    def move_to_submit_btn(self):
        submit_btn_locator = self.locators.SUBMIT_BTN
        submit_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(submit_btn_locator)
        )
        self.go_to_element(submit_btn)

    def click_submit_btn(self):
        self.driver.find_element(*self.locators.SUBMIT_BTN).click()
        return self


