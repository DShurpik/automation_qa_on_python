import pytest
from selenium import webdriver


@pytest.fixture(autouse=True, scope='function')
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield driver
    driver.quit()
