Client Quickstart (aiohttp)
https://docs.aiohttp.org/en/stable/client_quickstart.html

Python: FastAPI error 422 with POST
https://stackoverflow.com/questions/59929028/python-fastapi-error-422-with-post-request-when-sending-json-data

Python - convert image to JSON
https://stackoverflow.com/questions/54660800/python-convert-image-to-json

Open PIL image from byte file
https://stackoverflow.com/questions/32908639/open-pil-image-from-byte-file

Django Image Upload
https://www.javatpoint.com/django-image-upload
https://www.geeksforgeeks.org/python-uploading-images-in-django/



### Полезные команды:

> бращение к серверу с передачей аргументов в запросе:
http://127.0.0.1:8000/hello?name=OTUS&last_name=OCTOPUS
 
> Страница интерактивной документации (Swagger): 
http://127.0.0.1:8000/docs

How to check if port is in use:
```shell
sudo lsof -i -P -n | grep LISTEN
```

kill the process:
```shell
kill -9 id
```

Если есть ошибка рип установке `psycopg2`:
>ERROR: Failed building wheel for psycopg2

Установи недостающие зависимости:
```shell
sudo apt-get install libpq-dev python3-dev
```
```shell
sudo apt-get install gcc
```

Questions:
- How config `static(settings.MEDIA_URL` in prod?