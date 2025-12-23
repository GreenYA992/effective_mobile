import allure
import pytest

from pages.login_page import LoginPage
from utils.driver_factory import DriverFactory


@pytest.fixture(scope="function")
def driver():
    driver = DriverFactory.get_driver(headless=True)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver).open()
