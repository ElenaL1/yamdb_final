# yamdb_final CI CD
![yamdb_final](https://github.com/ElenaL1/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?event=push)

Запуск проекта через Github Actions.
Проект является продолжением проекта API для Yamdb https://github.com/ElenaL1/api_yamdb 
Проект упаковывается docker compose. Автор проекта: Елена Ламберт

## Стек
Python 3.9, Django, DRF, Simple-JWT, PostgreSQL, Ubuntu, Docker, nginx, gunicorn, Pandas, Github Actions, Yandex Cloud

## Workflow состоит из четырёх шагов:
    Проверка кода на соответствие PEP8
    Сборка и публикация образа бекенда на DockerHub.
    Автоматический деплой на удаленный сервер.
    Отправка уведомления в телеграм-чат.

## Как запустить проект:
Запускается при обновление репозитория (команда git push).

Проект доступен по адресу zali3.ddns.net


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
Более подробно информацию об эндпоинтах и примерах запросов и ответов можно посмотреть в
```yamdb_final/api_yamdb/api_yamdb/static/redoc.yaml```