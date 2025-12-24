# Docker
build:
    docker build -t effective_mobile-tests .
test:
    docker run --rm effective_mobile-tests
test_report:
	docker run --rm -v "./allure-report:/app/allure-report" effective_mobile-tests

# Docker_compose
compose_test:
    docker compose up --build