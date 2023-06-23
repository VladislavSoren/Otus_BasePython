
Преимущества запуска проекта, как сети из контенеров:
- Легче и быстрей развёртывать
- Докер сеть - это изолированная сеть (+ к безопасности)


Commands:
Запускаем контейнеры через 
```shell
docker compose up -d pg
```

Накатываем миграхи
```shell
flask db upgrade
```

Сборка образа из Докерфайла
```shell
docker build . -t app
```

Сборка образа из Докерфайла
```shell
docker build . -t app
```

Стопарим контейнеры И удаляем вольюмы
```shell
docker compose down -v
```

Собираем образ из контейнеров в yml файле
```shell
docker compose build app
```

Запускаем образ 
```shell
docker compose up app
```

Запускаем образ в detach режиме
```shell
docker compose up -d app
```

Запускаем образ 
```shell
docker container inspect <cont_name>
```

Зайти внутрь контейнера под его bash
```shell
docker compose exec -it app-dev bash
```


Notes:
- docker-compose уже встроен в docker, поэтому его отдельно не нужно накатывать
- Почти любую докер команду можно обернуть в docker-compose.yml
- healthcheck в docker-compose.yml
- NGINX запускается на 80 порту
- `head -19 templates/index.html |tail -1` - вывод конкретной строки
Проброс изменений в докер (чётко для отладки) 
- `volumes:
          ./:/app`


Important:
- `packages = [{include = "mega_shop"}]` нужно удалять из pyproject.toml, иначе
не собирается образ
- app.run(host="0.0.0.0", debug=True), т.к. localhost НЕ доступен снаружи
-  WARNING: This is a development server. Do not use it in a production deployment. 
Use a production WSGI server instead.

Fails:
    После того ка постучался в 8000 порт, то стали оживать другие порты, бред...

    Изначально с:
    ports:
      - "5000:80"
    Не было подключения