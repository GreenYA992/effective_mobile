import allure
import pytest

from pages.login_page import LoginPage
from utils.driver_factory import DriverFactory


# Регистрируем маркер
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "local: Тесты для локального запуска (браузер виден)"
    )
    config.addinivalue_line(
        "markers", "docker: Тесты для запуска в Docker (headless режим)"
    )


@pytest.fixture(scope="function")
def driver(request):

    local_marker = request.node.get_closest_marker("local") is not None
    docker_marker = request.node.get_closest_marker("docker") is not None

    if local_marker:
        headless = False  # Локально - браузер виден
    elif docker_marker:
        headless = True  # Docker - headless
    else:
        headless = True  # По умолчанию - для совместимости с Docker

    driver = DriverFactory.get_driver(headless=headless)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver).open()
