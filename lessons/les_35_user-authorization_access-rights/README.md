

## Signals:
- `post_save` signal for `OrderPaymentDetails` instance creating,
when Order is updated/created (save action)


## SharedTasks:
- send mail, when signal `post_save` from Order received 

## Access restrictions
- order list for non-authenticated users 
- donat list for non-authenticated users

## User:
- registration
- 

## Project start commands
Root level:
- `poetry install`
- `docker compose up -d`

Project level:
- `python manage.py migrate`
- `python manage.py runserver`
- `celery -A pro_platform worker -l INFO`

Alternative start:
- bash start_project.sh
- bash start_celery.sh
