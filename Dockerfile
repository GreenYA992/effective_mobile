FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    # утилита для скачивания файлов
    wget \
    # утилита для проверки файлов
    gnupg \
    # утилита для запросов
    curl \

    # проверяет программу на подлинность
    ca-certificates \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /etc/apt/trusted.gpg.d/google-chrome.gpg \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \

    # Установка chrome
    && apt-get update \
    && apt-get install -y google-chrome-stable \

    && rm -rf /var/lib/apt/lists/*
    # Чистим мусор

# -- Устанавливаем Java и утилиты
# Ставим движок Java + wget + unzip (распаковщик)
RUN apt-get update && apt-get install -y openjdk-21-jre-headless wget unzip \
    # Скачиваем и устанавливаем Allure
    && wget -q -O allure-commandline.zip https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.27.0/allure-commandline-2.27.0.zip \
    # Распаковываем в папку /opt/
    && unzip allure-commandline.zip -d /opt/ \
    # Создаем ярлык 'allure', чтобы можно было обращаться к 'allure' в консоли
    && ln -s /opt/allure-2.27.0/bin/allure /usr/bin/allure \
    # Удаляем zip
    && rm allure-commandline.zip \

    && rm -rf /var/lib/apt/lists/*
    # Чистим мусор

# Проверяем установку
RUN allure --version

RUN google-chrome-stable --version

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Запускаем тесты в headless режиме
CMD ["pytest", "tests/", "--alluredir=./allure-results"]