# FanatKG Pre-Beta

## Настройка сервера
Сервер: Ubuntu 20.04

Гайд по базовой настройке Ubuntu-сервера: https://github.com/vasilbekk/ubuntu-setup-django

## Установка и подключение PostgreSQL


### Заполнение переменных виртуального окружения
Теперь в корневой директории Django-проекта (core) создаем файл .env и записываем туда данные:
Переменная  | Назначение
------------- | -------------
`DATABASE_NAME`  | Название базы данных PostgreSQL
`DATABASE_USER` | Пользователь базы данных
`DATABASE_PASSWORD` | Пароль
`DATABASE_HOST` | Адрес БД, если на вашей машине, то 127.0.0.1
`DATABASE_PORT` | Порт, обычно 5432
`SECRET_KEY` | Секретный ключ Django


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


