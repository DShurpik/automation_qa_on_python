from pages.base_page import BasePage


class Tests:
    def test_open_page(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.open('https://www.google.com/')
