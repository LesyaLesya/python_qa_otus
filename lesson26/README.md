# Работа с Docker

1.Запустить Selenoid:
перейти в директорию с исполняемым файлов и выполнить команды:
```
./cm_darwin_amd64 selenoid start
./cm_darwin_amd64 selenoid-ui start
```
+добавить нужные браузеры в файл .aerokube/selenoid/browsers.json

2.В консоли перейти в директорию с файлом Dockerfile

3.Выполнить команду для создания образа с тегом:
```
docker build -t tests .
```
4.Посмотреть созданный образ: 
```
docker images
```
4.Запустить тесты
(могут быть проблемы с импортируемыми модулями - обратить внимание на пути.
Можно задать путь от созданной рабочей директории внутри контейнера - /app).

Команда для просмотра адреса в сети - ifconfig
```
docker run --rm tests --browser_name chrome --browserVersion 86.0 --executor адрес_компа_в_сети
```
5.Запуск тестов + отчет
В консоли выполнить команду, в качестве параметра указав внешний адрес selenoid и путь до исполняемого файла allure на вашей машине:

```
./allure.sh selenoid_host /path/to/allure/bin
Пример: ./allure.sh external_ip_selenoid /Applications/allure/bin/allure
```
