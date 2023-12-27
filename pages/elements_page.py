import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators
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

class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_all_checkboxes(self):
        self.driver.find_element(*self.locators.EXPAND_ALL_BTN).click()

    def click_random_item(self):
        item_list = self.driver.find_elements(*self.locators.ITEM_LIST)
        item = item_list[random.randint(1, 15)]
        item.click()

    # Use value from locators.fields.CheckBoxPageValues for clicking different checkboxes
    def click_on_checkbox(self, field):
        self.driver.find_element(By.XPATH, f'//span[text()="{field}"]').click()

    def get_result_string(self):
        result = self.driver.find_element(*self.locators.RESULT).text
        data_res = result.split(',')
        print(data_res)
        return data_res

    def get_checked_checkboxes(self):
        checked_list = self.driver.find_elements(*self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.driver.find_elements(*self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_radio_btn(self, field):
        self.driver.find_element(By.XPATH, f'//label[text()="{field}"]').click()

    def get_result(self):
        result = self.driver.find_element(*self.locators.RESULT_FIELD).text
        return result




