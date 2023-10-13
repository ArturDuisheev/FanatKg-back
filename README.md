# FanatKG Pre-Beta

## Настройка сервера
Сервер: Ubuntu 20.04

Гайд по базовой настройке Ubuntu-сервера: https://github.com/vasilbekk/ubuntu-setup-django

## Установка и подключение PostgreSQL


### Заполнение переменных виртуального окружения
Теперь в корневой директории Django-проекта (core) создаем файл .env и записываем туда данные:
Переменная  | Назначение
------------- | -------------
`POSTGRES_DB`  | Название базы данных PostgreSQL
`POSTGRES_USER` | Пользователь базы данных
`POSTGRES_PASSWORD` | Пароль
`POSTGRES_HOST` | Адрес БД, если на вашей машине, то 127.0.0.1
`POSTGRES_PORT` | Порт, обычно 5432
`SECRET_KEY` | Секретный ключ Django
`ALLOWED_HOSTS` | Доступные хосты для подключения к серверу
`PRODUCTION` | Если Production=False, то база данных будет изменена на sqlite и DEBUG=TRUE, а если Production=True, то бд psql и DEBUG=False.
`CORS_ALLOWED_ORIGINS` | это конфигурационный параметр в Django, определяющий список разрешенных источников (доменов), из которых можно отправлять кросс-оригин (CORS) HTTP-запросы к вашему веб-приложению.



### Выполняем миграции и запуск
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```


### Docker, docker-compose команды
Это памятка команд на случай если в проекте будет docker
Команда     | Назначение
------------- | -------------
`docker-compose -f <ваш docker-compose.yml> up -d --build`  | Запуск всех контейнеров
`docker-compose -f <ваш docker-compose.yml> down -v` | останавливает и удаляет контейнеры.
`docker-compose -f <ваш docker-compose.yml> up -d --no-deps --build <имя образа> ` | запускает контейнер из указанного образа, используя конфигурацию из файла docker-compose.yml.
`docker-compose -f <ваш docker-compose.yml> logs <имя образа>` | Эта команда дает логи(ответ сервера)
`docker ps` | позволяет смотреть запущенные вами образы
`docker-compose exec <имя образа> <команда> ` | для выполнения команды внутри контейнера, определенного в файле docker-compose.yml. Например, команда "docker-compose exec <вашего контейнера> python manage.py runserver" выполнит команду "python manage.py runserver" внутри вашего контейнера, который определен в файле docker-compose.yml.


