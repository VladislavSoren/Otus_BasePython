### ORM (Object-relational mapping) - инструмент, который позволяет связать объекты в коде с объектами в БД.

### Запреты:
    * Никогда не форматировать данный для SQL запроса (ни f-строчкой, ни чем либо ещё)
        * нужно через VALUES(?, ?) и другие внутренние средства
    * При использовании ORM все эти косяки невилируются

Если есть ошибка рип установке `psycopg2`:
>ERROR: Failed building wheel for psycopg2

Установи недостающие зависимости:
```shell
sudo apt-get install libpq-dev python3-dev
```

To Do list:
* Установить Zsh в Ubuntu (красивая подсветка в терминале)
* Авто black in PyCharm
* Починить koncert_bot (прописать модуль url_checker)