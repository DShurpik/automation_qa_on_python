from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def navigate_to(self, field):
        self.driver.find_element(By.XPATH, f'//div//h5[text()="{field}"]').click()

    def navigate_to_in_menu_list(self, field):
        self.driver.find_element(By.XPATH, f'//span[text()="{field}"]').click()

    def get_created_value(self, locator):
        result =self.driver.find_element(*locator).text
        return result

    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def go_to_element(self, element):
        self.driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - 300);", element)

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
