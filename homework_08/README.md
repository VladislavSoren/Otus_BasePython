# Направление для Django проекта: `Профессиональная платформа`
(`Планируется сделать на базе данной темы проектную работу`)

Создано приложение в рамках выбранного проекта `магазин проектов`
## Модели:
- Creator
- Category
- Project
- Donat


## Алгоритм запуска проекта:
- На уровне `docker-compose.yml` запускаем БД (postgres) командой `docker compose up`
- На уровне `pro_platform` создаём коммиты миграций `python manage.py makemigrations`
- Выполняем миграции `python manage.py migrate`
- Запускаем проект ` python manage.py runserver`