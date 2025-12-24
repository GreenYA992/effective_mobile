from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverFactory:
    @staticmethod
    def get_driver(
        browser="chrome", headless=True
    ):  # False - Локально True - для Docker
        if browser.lower() == "chrome":
            options = Options()
            if headless:
                options.add_argument("--headless")

            # Обязательные опции для Docker
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            # Только FATAL ошибки
            options.add_argument("--log-level=3")
            # Отключаем видеокарту, только процессор
            options.add_argument("--disable-gpu")
            # Размер окна браузера
            options.add_argument("--window-size=1920,1080")
            # Поиск драйвера
            driver = webdriver.Chrome(options=options)
        else:
            raise ValueError(f"Browser {browser} not supported")

        driver.implicitly_wait(10)
        return driver
