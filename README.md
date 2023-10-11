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


### Выполняем миграции
```
$ python manage.py makemigrations
$ python manage.py migrate
```

## Redis
Устанавливаем Redis:
```
sudo apt-get install redis-server
```

Отключаем автозапуск, чтобы не запускался
```
$ sudo systemctl disable redis-server
$ sudo systemctl stop redis-server
```

Создаём файл конфигурации на основе сэмпла
```
$ cp /home/www/taxiber/telegram_bot/data/redis.conf.sample /home/www/taxiber/telegram_bot/data/redis.conf
```

Заполняем конфигурационные данные `redis.conf`
```
...
logfile <logfile_path>
...
dir <work_dir_path>
...
```

Запускаем Redis
```
$ redis-server /home/www/taxiber/telegram_bot/data/redis.conf
```


