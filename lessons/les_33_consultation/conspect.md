
Можно доставать статусы задач из таблицы
`django_celery_results_taskresult` с помощью
встроенных инструментов


Summary:
- Возможно сделать красивую доставку писем при отладке
(чем лучше логов?)
- Документация по настройке писем:
https://docs.djangoproject.com/en/4.2/topics/email/
- django-mail-templated

Notes:
- SMTP (Simple Mail Transfer Protocol) — простой протокол передачи почты)
- Каскадное создание через сигналы
- Для создания индекса для поля указываем атрибут `db_index = True`
- для ускорения работы нужно их создавать для полей с частым поиском!

Commands:

Install main dependencies and delete others
```shell
poetry install --only-main --sync
```

Create auto empty migration
```shell
python manage.py makemigrations shop_projects --empty
```

```