import time

from basePages.base_page import BasePage
from basePages.base_test import BaseTest
from config_reader.config import ConfigProvider
from locators.fields import Fields
from pages.elements_page import TextBoxPage
from locators.elements_page_locators import TextBoxPageLocators


class Tests(BaseTest):

    def test_open_page(self, driver):
        base_page = BasePage(driver)
        base_page.open('https://www.google.com/')

    def test_text_box_hard_code(self, driver):
        text_box_page = TextBoxPage(driver)
        text_box_page.open('http://85.192.34.140:8081')
        time.sleep(1)
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
        time.sleep(1)
        text_box_page.navigate_to(Fields.ELEMENTS)
        text_box_page.navigate_to_in_menu_list(Fields.TEXT_BOX)
        text_box_page.fill_full_name_fields(config.get('User', 'Full_Name'))
        text_box_page.fill_email_fields(config.get('User', 'Email'))
        text_box_page.fill_current_address_fields(config.get('User', 'Current_Address'))
        text_box_page.fill_permanent_address_fields(config.get('User', 'Permanent_Address'))
        text_box_page.click_submit_btn()
        time.sleep(3)
