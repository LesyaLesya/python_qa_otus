1.Запустить Selenoid:
перейти в директорию с исполняемым файлом и выполнить команды:
```
./cm_darwin_amd64 selenoid start
./cm_darwin_amd64 selenoid-ui start
```
2.Запустить Open Cart

Значение для OPENCART_HOST передается в командной строке через переменную local_ip - адрес вашей машины в сети
(узнать через ifconfig)

```
local_ip=123.123.123.123 docker-compose up -d
```

3.Запустить тесты 

(в параметре URL передать адрес вашей машины в сети,
в параметре BROWSER передать браузер)
```
robot -v URL:123.123.123.123 -d Results/ Tests/
```
 
4.Запустить тесты с генерацией отчетов в Allure
```
robot -v URL:123.123.123.123 -d Results/ --listener allure_robotframework Tests/
```

5.Посмотреть отчет
В консоли выполнить команду, в качестве параметра указав путь до исполняемого файла allure на вашей машине:

```
lesson30_31/allure.sh /path/to/allure/bin
Пример: lesson30_31/allure.sh /Applications/allure/bin/allure
```
