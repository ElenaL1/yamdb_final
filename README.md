# yamdb_final CI CD
![yamdb_final](https://github.com/ElenaL1/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?event=push)

Запуск проекта через Github Actions.
Проект является продолжением проекта API для Yamdb https://github.com/ElenaL1/api_yamdb 
Проект упаковывается docker compose. Автор проекта: Елена Ламберт

## Стек
Python 3.9, Django, DRF, Simple-JWT, PostgreSQL, Ubuntu, Docker, nginx, gunicorn, Pandas, Github Actions, Yandex Cloud

## Как запустить проект:

На сервере на Linux Ubuntu нужно установить docker и docker-compose. Скопировать на сервер файлы docker-compose.yaml и nginx/default.conf:
```
scp docker-compose.yaml <логин_на_сервере>@<IP_сервера>:/home/<логин_на_сервере>/docker-compose.yaml
scp default.conf <логин_на_сервере>@<IP_сервера>:/home/<логин_на_сервере>/nginx/default.conf
```

## Workflow состоит из четырёх шагов:
    Проверка кода на соответствие PEP8 и pytest
    Сборка и публикация образа бекенда на DockerHub.
    Автоматический деплой на удаленный сервер.
    Отправка уведомления в телеграм-чат.

Далее на сервере нужно запустить следущие команды (выполнить миграции, создать суперпользователя, собрать статитку):
```
sudo docker-compose exec web python manage.py migrate
sudo docker-compose exec web python manage.py createsuperuser
sudo docker-compose exec web python manage.py collectstatic --no-input
```

Деплой сервера запускается при обновление репозитория (команда git push).

Проект доступен по [адресу](http://zali3.ddns.net/api/v1/)


## Примеры запросов
Пример POST-запроса на регистрацию нового пользователя: POST .../api/v1/auth/signup/
```
{
"email": "user@example.com",
"username": "string"
}
```
Пример ответа на GET-запрос на получение списка всех произведений: GET .../api/v1/titles/
```
{
"count": 0,
"next": "string",
"previous": "string",
"results": [
{
"id": 0,
"name": "string",
"year": 0,
"rating": 0,
"description": "string",
"genre": [
{
"name": "string",
"slug": "string"
}
],
"category": {
"name": "string",
"slug": "string"
}
}
]
}
```
Более подробно информацию об эндпоинтах и примерах запросов и ответов можно посмотреть по 
[ссылке](http://zali3.ddns.net/redoc/)