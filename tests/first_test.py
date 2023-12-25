import time

from basePages.base_page import BasePage
from basePages.base_test import BaseTest
from config_reader.config import ConfigProvider
from generator.generator import person_generator
from locators.fields import Fields, CheckBoxPageValues
from pages.elements_page import TextBoxPage, CheckBoxPage
from locators.elements_page_locators import TextBoxPageLocators


class Tests(BaseTest):

    def test_open_page(self, driver):
        base_page = BasePage(driver)
        base_page.open('https://www.google.com/')

    def test_text_box_hard_code(self, driver):
        text_box_page = TextBoxPage(driver)
        text_box_page.open('http://85.192.34.140:8081')
        text_box_page.navigate_to(Fields.ELEMENTS)
        text_box_page.navigate_to_in_menu_list(Fields.TEXT_BOX)
        text_box_page.fill_full_name_fields('D S')
        text_box_page.fill_email_fields('Ds@ds.ru')
        text_box_page.fill_current_address_fields('Minsk')
        text_box_page.fill_permanent_address_fields('Minsk')
        text_box_page.click_submit_btn()

        result_full_name = text_box_page.get_created_value(TextBoxPageLocators.CREATED_NAME_FIELD).split(':')[1]
        result_email = text_box_page.get_created_value(TextBoxPageLocators.CREATED_EMAIL_FIELD).split(':')[1]
        result_current_address = text_box_page.get_created_value(TextBoxPageLocators.CREATED_CURRENT_ADDRESS_FIELD).split(':')[1]
        result_permanent_address = text_box_page.get_created_value(TextBoxPageLocators.CREATED_PERMANENT_ADDRESS_FIELD).split(':')[1]

        assert result_full_name == "D S", f"Expected 'D S', but got {result_full_name}"
        assert result_email == "Ds@ds.ru", f"Expected 'D S', but got {result_email}"
        assert result_current_address == "Minsk", f"Expected 'D S', but got {result_current_address}"
        assert result_permanent_address == 'Minsk', f"Expected 'D S', but got {result_permanent_address}"

    def test_text_box_use_conf(self, driver):
        text_box_page = TextBoxPage(driver)
        config = ConfigProvider().read_config('apps')
        text_box_page.open('http://85.192.34.140:8081')
        text_box_page.navigate_to(Fields.ELEMENTS)
        text_box_page.navigate_to_in_menu_list(Fields.TEXT_BOX)
        text_box_page.fill_full_name_fields(config.get('User', 'Full_Name'))
        text_box_page.fill_email_fields(config.get('User', 'Email'))
        text_box_page.fill_current_address_fields(config.get('User', 'Current_Address'))
        text_box_page.fill_permanent_address_fields(config.get('User', 'Permanent_Address'))
        text_box_page.click_submit_btn()

        result_full_name = text_box_page.get_created_value(TextBoxPageLocators.CREATED_NAME_FIELD).split(':')[1]
        result_email = text_box_page.get_created_value(TextBoxPageLocators.CREATED_EMAIL_FIELD).split(':')[1]
        result_current_address = \
        text_box_page.get_created_value(TextBoxPageLocators.CREATED_CURRENT_ADDRESS_FIELD).split(':')[1]
        result_permanent_address = \
        text_box_page.get_created_value(TextBoxPageLocators.CREATED_PERMANENT_ADDRESS_FIELD).split(':')[1]

        assert result_full_name == "Dzmitry S", f"Expected 'D S', but got {result_full_name}"
        assert result_email == "ds@gmail.com", f"Expected 'D S', but got {result_email}"
        assert result_current_address == "Minsk", f"Expected 'D S', but got {result_current_address}"
        assert result_permanent_address == 'Minsk', f"Expected 'D S', but got {result_permanent_address}"

    def test_text_box_use_faker(self, driver):
        user = next(person_generator())

        full_name = user.full_name
        email = user.email
        current_address = user.current_address
        permanent_address = user.permanent_address

        text_box_page = TextBoxPage(driver)
        text_box_page.open('http://85.192.34.140:8081')
        text_box_page.navigate_to(Fields.ELEMENTS)
        text_box_page.navigate_to_in_menu_list(Fields.TEXT_BOX)
        text_box_page.fill_full_name_fields(full_name)
        text_box_page.fill_email_fields(email)
        text_box_page.fill_current_address_fields(current_address)
        text_box_page.fill_permanent_address_fields(permanent_address)
        text_box_page.click_submit_btn()

        result_full_name = text_box_page.get_created_value(TextBoxPageLocators.CREATED_NAME_FIELD).split(':')[1]
        result_email = text_box_page.get_created_value(TextBoxPageLocators.CREATED_EMAIL_FIELD).split(':')[1]
        result_current_address = \
            text_box_page.get_created_value(TextBoxPageLocators.CREATED_CURRENT_ADDRESS_FIELD).split(':')[1]
        result_permanent_address = \
            text_box_page.get_created_value(TextBoxPageLocators.CREATED_PERMANENT_ADDRESS_FIELD).split(':')[1]

        assert result_full_name == full_name, f"Expected 'D S', but got {result_full_name}"
        assert result_email == email, f"Expected 'D S', but got {result_email}"
        assert result_current_address == current_address, f"Expected 'D S', but got {result_current_address}"
        assert result_permanent_address == permanent_address, f"Expected 'D S', but got {result_permanent_address}"

    def test_checkbox_click_randomly(self, driver):
        check_box_page = CheckBoxPage(driver)

        check_box_page.open('http://85.192.34.140:8081/')
        check_box_page.navigate_to(Fields.ELEMENTS)
        check_box_page.navigate_to_in_menu_list(Fields.CHECK_BOX)
        check_box_page.open_all_checkboxes()
        check_box_page.click_random_item()

        result1 = check_box_page.get_checked_checkboxes()
        result2 = check_box_page.get_output_result()

        assert result1 == result2

    def test_checkbox_click_value(self, driver):
        check_box_page = CheckBoxPage(driver)

        check_box_page.open('http://85.192.34.140:8081/')
        check_box_page.navigate_to(Fields.ELEMENTS)
        check_box_page.navigate_to_in_menu_list(Fields.CHECK_BOX)
        check_box_page.open_all_checkboxes()

        check_box_page.click_on_checkbox(CheckBoxPageValues.DOCUMENTS)

        result1 = check_box_page.get_checked_checkboxes()
        result2 = check_box_page.get_output_result()

        assert result1 == result2

    def test_checkbox_click_value2(self, driver):
        check_box_page = CheckBoxPage(driver)

        check_box_page.open('http://85.192.34.140:8081/')
        check_box_page.navigate_to(Fields.ELEMENTS)
        check_box_page.navigate_to_in_menu_list(Fields.CHECK_BOX)
        check_box_page.open_all_checkboxes()
        check_box_page.click_on_checkbox(CheckBoxPageValues.DOCUMENTS)

        result1 = check_box_page.get_checked_checkboxes()
        result2 = check_box_page.get_output_result()

        assert result1 == result2

        time.sleep(1)