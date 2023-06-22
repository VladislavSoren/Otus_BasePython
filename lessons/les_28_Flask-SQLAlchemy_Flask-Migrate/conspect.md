Макрос - шаблон и функция

Flask-WTF - Simple integration of Flask and WTForms, 
including CSRF, file upload, and reCAPTCHA.

Notes:
- Никогда НЕ делать импорты из главного модуля. Познакомься
с моим маленьким циклическим импортом Гарри.
- Обязательно импортировать в init классы таблиц, чтобы миграха увидела схемы!
- CSRF protection (The CSRF token is missing :) -> Защита от публикации формы от
нашего имени с левого сайта
- Валидацию полей так же красиво можно сделать через фронтенд (Bootstrap)

Commands:
Инициализация миграций (Аналогично `alembic init`)
```shell
flask db init
```

Создастся база (но пустая)
```shell
flask db current
```

Создание миграхи (НЕ примененной)
```shell
flask db migrate -m "create products table"
```

Добавляем black в группу разработки (Зависимости)
```shell
poetry add black --group dev
```
 
Накатываем миграхи
```shell
flask db upgrade
```
