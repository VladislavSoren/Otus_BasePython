
Commands:
Adding package to dev group
```shell
poetry add django-debug-toolbar --group dev
```

Do not update locked versions, only refresh lock file (if new packages will be added)
```shell
poetry lock --no-update
```

Install main dependencies and delete others
```shell
poetry install --only-main --sync
```

Create auto empty migration
```shell
python manage.py makemigrations shop_projects --empty
```

To know ur IP
```shell
ip a
```

link to shell under django
```shell
python manage.py shell
```

link to shell under debug django (in DebugToolbar set)
```shell
python manage.py debugsqlshell
```