# Описание проекта
Автоматизированное тестирование сценариев авторизации 
на сайте https://www.saucedemo.com/ 
с использованием Python, Selenium, Page Object Pattern и Allure отчетов.

### Технологический стек
- Python 3.10
- Selenium 4.33.0 - автоматизация браузера
- pytest 9.0.1 - фреймворк для тестирования
- pytest-xdist 3.8.0 - параллельный запуск тестов
- Allure-pytest 2.15.2 - генерация отчетов
- Docker - контейнеризация тестов

### Тестовые сценарии
- Успешный логин (standard_user / secret_sauce)
- Логин с неверным паролем
- Логин заблокированного пользователя (locked_out_user)
- Логин с пустыми полями
- Логин пользователем performance_glitch_user

# Локальный запуск
- ### Установка зависимостей
```bash
pip install -r requirements.txt
```
- ### Запуск тестов
- ##### Только локальные тесты
```bash
pytest tests/ -m local
```
- ##### Полный цикл (тесты + отчет (На ПК не установлен Allure, не проверял))
```bash
pytest tests/ -m local --alluredir=./allure-results && allure generate ./allure-results --clean -o ./allure-report
```

# Запуск в Docker
- ### Сборка Docker образа
```bash
docker build -t effective_mobile-tests .
```
- ### Запуск тестов
```bash
docker run --rm -e DOCKER_MODE=true effective_mobile-tests
```
- ### Запуск тестов с отчетами
```bash
docker run --rm -v "./allure-report:/app/allure-report" -e DOCKER_MODE=true effective_mobile-tests
```

# Запуск через docker-compose
- ### Полный цикл (тесты + отчет)
```bash
docker compose up --build
```