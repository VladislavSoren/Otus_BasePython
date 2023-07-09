Algorithm updating user password from debug shell:
1. from django.contrib.auth.models import User
2. sam = User.objects.filter(username="sam").get()
3. sam.set_password("123")
4. sam.save()

Adding new app:
1. Creating
2. adding `auth.apps.AuthConfig` to settings.py of project 
3. create urls.py
4. add url of app in main urls.py of project 

Commands:
Enter in debug shell
```shell
python manage.py debugsqlshell
```
creating new app
```shell
python manage.py startapp auth
```


ToDoList:
- Creating OrderPaymentDetails when it fill
togather with Order (adminka)



