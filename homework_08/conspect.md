Algorithm for creating a signal:
- Используем сигнал `post_save` (нужно учитывать: после сохранения изм-ий или создания)
- Создаём функцию под декоратором `receiver`, отправителем ставим `Order`
- Функция принимает параметры:
    - instance: Order (экземпляр класса, который будет сохранён)
    - created: bool (если True, то только при создании новой записи)
- `if created: OrderPaymentDetails.objects.get_or_create(order=instance)`


Алгоритм запуска CELERY (инструмент для выполнения отложенных задач): 
https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html

Algorithm of creating shared_task (mailing example):
- `poetry add celery`
- celery setting (Follow celery instruction):
  - create celery.py in project dir (pro_platform)
  - import celery in __init__.py of project
  - add config parameters  in setting.py
  - creating tasks.py files in our apps (shop_projects)
  - in this file create @shared_task function
  - add created func in signal function in models.py file (on_order_save)
  * with delay method
- django-celery-results setting (Follow celery instruction):
  - `poetry add django-celery-results`
  - updated setting.py (CELERY_BROKER_URL..,)
  - migrate
- run celery for task completion by `celery -A pro_platform worker -l INFO` 
- Setting templates for mail:
  - `poetry add django-mail-templated`
  - add this app in settings.py
  - in @shared_task function add `send_mail` from mail_templated
  - create email/order-updated.html template
- initiate signal (add/update and `save` order)

ToDoList:
- Creating OrderPaymentDetails when it fill
togather with Order (adminka)



