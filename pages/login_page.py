from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def open(self):
        """Открываем страницу"""
        self.driver.get("https://www.saucedemo.com/")
        return self

    def enter_username(self, username):
        """Вводим логин в поле Username"""
        element = self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT))
        element.clear()
        element.send_keys(username)
        return self

    def enter_password(self, password):
        """Вводим пароль в поле Password"""
        element = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        element.clear()
        element.send_keys(password)
        return self

    def click_login(self):
        """Нажимаем кнопку Login"""
        element = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        element.click()
        return self

    def login(self, username, password):
        """Выполняем процесс авторизации"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def get_error_message(self):
        """Получаем текст сообщения об ошибке"""
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return element.text
        except TimeoutException:
            return None

    def is_page_displayed(self):
        """Проверяем, отображается ли страница, после успешного логина"""
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self.INVENTORY_CONTAINER)
            )
            return element.is_displayed()
        except TimeoutException:
            return False

    def get_current_url(self):
        """Возвращаем текущий URL страницы"""
        return self.driver.current_url
