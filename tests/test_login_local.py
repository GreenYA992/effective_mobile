import allure
import pytest

from pages.login_page import LoginPage


@allure.feature("Авторизация")
@allure.story("Успешная авторизация")
@pytest.mark.local
def test_successful_login(login_page):
    """Тест успешной авторизации с валидными данными"""
    with allure.step("Вводим логин и пароль пользователя"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Проверяем, что произошел переход на страницу"):
        assert login_page.is_page_displayed(), "Страница не отображается"

    with allure.step("Проверяем URL страницы"):
        assert (
            "/inventory.html" in login_page.get_current_url()
        ), "Некорректный URL после авторизации"


@allure.feature("Авторизация")
@allure.story("Неуспешная авторизация с неверным паролем")
@pytest.mark.local
def test_login_with_wrong_password(login_page):
    """Тест авторизации с неверным паролем"""
    with allure.step("Вводим логин пользователя и !!! некорректный !!! пароль"):
        login_page.login("standard_user", "wrong_password")

    with allure.step("Проверяем сообщение об ошибке"):
        error_message = login_page.get_error_message()
        assert error_message is not None, "Сообщение об ошибке не отображается"
        assert (
            "Username and password do not match" in error_message
        ), "Некорректное сообщение об ошибке"

    with allure.step("Проверяем, что остались на странице логина"):
        assert "/" in login_page.get_current_url(), "Переход с страницы логина"


@allure.feature("Авторизация")
@allure.story("Авторизация заблокированного пользователя")
@pytest.mark.local
def test_locked_out_user(login_page):
    """Тест авторизации заблокированного пользователя"""
    with allure.step("Вводим логин и пароль !!! заблокированного !!! пользователя"):
        login_page.login("locked_out_user", "secret_sauce")

    with allure.step("Проверяем сообщение об ошибке"):
        error_message = login_page.get_error_message()
        assert error_message is not None, "Сообщение об ошибке не отображается"
        assert (
            "Sorry, this user has been locked out" in error_message
        ), "Некорректное сообщение об ошибке"

    with allure.step("Проверяем, что остались на странице логина"):
        assert "/" in login_page.get_current_url(), "Переход с страницы логина"


@allure.feature("Авторизация")
@allure.story("Авторизация с пустыми полями")
@pytest.mark.local
def test_login_with_empty_fields(login_page):
    """Тест авторизации с пустыми полями"""
    with allure.step("Нажимаем кнопку Login без заполнения полей"):
        login_page.click_login()

    with allure.step("Проверяем сообщение об ошибке"):
        error_message = login_page.get_error_message()
        assert error_message is not None, "Сообщение об ошибке не отображается"
        assert (
            "Username is required" in error_message
        ), "Некорректное сообщение об ошибке"

    with allure.step("Проверяем, что остались на странице логина"):
        assert "/" in login_page.get_current_url(), "Переход с страницы логина"


@allure.feature("Авторизация")
@allure.story("Авторизация пользователя с задержками")
@pytest.mark.local
def test_performance_glitch_user(login_page):
    """Тест авторизации пользователя performance_glitch_user"""
    with allure.step("Вводим логин и пароль пользователя performance_glitch_user"):
        login_page.login("performance_glitch_user", "secret_sauce")

    with allure.step(
        "Проверить, что произошел переход на страницу инвентаря, несмотря на возможные задержки"
    ):
        assert login_page.is_page_displayed(), "Страница инвентаря не отображается"

    with allure.step("Проверить URL страницы"):
        assert (
            "/inventory.html" in login_page.get_current_url()
        ), "Некорректный URL после авторизации"