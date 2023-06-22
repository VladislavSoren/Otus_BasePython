
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

Notes:
- docker-compose уже встроен в docker, поэтому его отдельно не нужно накатывать
- Почти любую докер команду можно обернуть в docker-compose.yml
 
Important:
- `packages = [{include = "mega_shop"}]` нужно удалять из pyproject.toml, иначе
не собирается образ
- app.run(host="0.0.0.0", debug=True), т.к. localhost НЕ доступен снаружи