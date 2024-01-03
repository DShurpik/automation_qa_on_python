import random

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generator.generator import person_generator
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablesLocators, ButtonPageLocators
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


class WebTables(BasePage):
    locators = WebTablesLocators()

    def click_add_button(self):
        self.driver.find_element(*self.locators.ADD_BTN).click()

    def send_first_name_field(self, name):
        self.driver.find_element(*self.locators.FIRST_NAME_FIELD).send_keys(name)

    def send_last_name_field(self, last_name):
        self.driver.find_element(*self.locators.LAST_NAME_FIELD).send_keys(last_name)

    def send_email_field(self, email):
        self.driver.find_element(*self.locators.EMAIL_FIELD).send_keys(email)

    def send_age_field(self, age):
        self.driver.find_element(*self.locators.AGE_FIELD).send_keys(age)

    def send_salary_field(self, salary):
        self.driver.find_element(*self.locators.SALARY_FIELD).send_keys(salary)

    def send_department_field(self, department_name):
        self.driver.find_element(*self.locators.DEPARTMENT_FIELD).send_keys(department_name)

    def click_submit_btn(self):
        self.driver.find_element(*self.locators.SUBMIT_BTN).click()

    def check_person(self):
        persons_list = self.driver.find_elements(*self.locators.FULL_PERSONS_LIST)
        data = []
        for item in persons_list:
            data.append(item.text.splitlines())
        return data

    def check_search_person(self):
        persons_list = self.driver.find_elements(*self.locators.FULL_PERSONS_LIST)
        data = []
        for item in persons_list:
            data.append(item.text.splitlines())
        return data

    def send_search_parameter(self, name):
        self.driver.find_element(*self.locators.SEARCH_FIELD).send_keys(name)

    def click_edit_button(self):
        self.driver.find_element(*self.locators.EDIT_BTN).click()

    def update_person_inf(self):
        new_person_info = next(person_generator())
        age = new_person_info.age
        self.driver.find_element(*self.locators.AGE_FIELD).clear()
        self.driver.find_element(*self.locators.AGE_FIELD).send_keys(age)
        return str(age)

    def click_delete_btn(self):
        self.driver.find_element(*self.locators.DELETE_BTN).click()


class ButtonPage(BasePage):
    locators = ButtonPageLocators()

    def click_click_me(self):
        self.driver.find_element(*self.locators.CLICK_ME_BTN).click()

    def click_right_click(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self.locators.RIGHT_CLICK_BTN))
        action.context_click(self.driver.find_element(*self.locators.RIGHT_CLICK_BTN))
        action.perform()

    def double_click(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self.locators.DOUBLE_CLICK_BTN))
        action.double_click(self.driver.find_element(*self.locators.DOUBLE_CLICK_BTN))
        action.perform()

    def check_result(self):
        result = self.driver.find_element(*self.locators.RESULT).text
        return result
