# Django project name: `Professional platform`


## App #1: `shop projects`
## Models:
- Creator
- Category
- Project
- Donat


## Project start commands
Root level:
- `docker compose up -d`
- `docker compose -f docker-compose_rabbit.yml up -d`

Project level:
- `python manage.py migrate`
- `python manage.py runserver`
- `celery -A pro_platform worker -l INFO`

Alternative start:
- bash start_project.sh
- bash start_celery.sh
