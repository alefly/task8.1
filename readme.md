### Задание 8.1

Инструкция:

1. Команда "make file" - создает образ контейнера alefly/server:v1

2. Команда "make run" - создает контейнер из образа alefly/server:v1 и дает контейнеру имя server

3. Команда "make stop" - останавливает контейнер server

4. Команда "make start" - запускает контейнер server

5. Команда "make healthcheck" выводит информацию о версиях пакетов, необходимых для работы 1-4 команд, или инормацию о том, что пакеты не установлены.


Скрипт сервера лежит в папке copy 
Логи сервера внутри докера сохраняются в файл /var/log/server.log, из системы их можно посмотреть в папке /var/lib/docker
