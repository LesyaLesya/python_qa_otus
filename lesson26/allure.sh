#!/bin/bash

# Собираем image с тегом tests
docker build -t tests .


# Запускаем контейнер под именем my_container из image tests
docker run --rm --name my_container tests --browser_name chrome --browserVersion 87.0 --executor $1 -n 2

# Копируем из контейнера созданный allure-report
docker cp my_container:/lesson26/allure-report .

# Запускаем хост для отчёта аллюр (утилита лежит локально)
# Хост отчёта нужно будет остановить руками
$2 serve allure-report

# Удаляем из системы созданный контейнер
docker system prune -f
