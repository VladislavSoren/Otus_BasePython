Django, FasAPI, Flask используются для создания:
- WEB - приложений
- API

Django:
- Встроенная работа с БД
- Работа с формами
- CSRF защита
- Система авторизации
- Миграции
- Админка
- Система permission (кому что дозволено)
- Generics (подготовленные вьюшки)
- Встроенные в тесты работы с фикстурами
- Работа с email
- SEO
* Во Flask почти всё это ставится отдельными пакетами

Минусы:
- Меньшая гибкость
- Много ограничений
- Только ведётся работа над асинком

Плюсы:
- Ограничения направляют делать приложение "правильно"

Описание:
- Папка проекта (sales_shop) и папка приложения (shop) - разные вещи
- Django подход (MTV): 
  - Fat models
  - Thin views
  - Stupid templates
- в проде статику обязан обслуживать веб сервер (NGINX или другой)


Notes:
- Django Rest framework (для написания реактивного приложения)
- Часто cдают на проектную работу на Django 
- Некоторые крнитерии оценки ПР:
  - Работа с пользователями 
  - авторизация 
  - доступы
  - работа с web
- Werkzeug (на нём Flask) - библиотека, т.к. предоставляет набор инструментов (и мы сами себе хозяева),
а Flask под капотом дофига сам делает много за нас (маршрутизацию и т.п.)
- jinja2 в Jango уже нет (Python в HTML капут) 
- ls -off (прослушка портов)
- Плюсон к FastAPI
- Микросервис - маленькая софтина, которая решает конкретную задачу, например по координатам определить
ваш часовой поест (капец упращённо)
- 


Questions:
- Что такое реактивное приложение? 
- Как сделать restart always in docker compose
- Какие плюшки от админки?
- Выбор фреймворка может зависеть от политики в компании, либо так больше нравится (бред...)

Commands:
Creating project
```shell
python -m django startproject pro_platform
```

Starting project
```shell
python manage.py runserver
```

Run migrations
```shell
python manage.py migrate
```

Creating app
```shell
python manage.py startapp shop_projects
```

Create migrations
```shell
python manage.py makemigrations
```

Create superuser for admin mode
```shell
python manage.py createsuperuser
```