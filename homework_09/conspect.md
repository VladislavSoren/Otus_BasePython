Client Quickstart (aiohttp)
https://docs.aiohttp.org/en/stable/client_quickstart.html

Python: FastAPI error 422 with POST
https://stackoverflow.com/questions/59929028/python-fastapi-error-422-with-post-request-when-sending-json-data

Python - convert image to JSON
https://stackoverflow.com/questions/54660800/python-convert-image-to-json

Open PIL image from byte file
https://stackoverflow.com/questions/32908639/open-pil-image-from-byte-file

Если программу (модуль, библиотеку) рассматривать как чёрный ящик, 
то API — это набор «ручек», которые доступны пользователю данного ящика и 
которые он может вертеть и переключать.

Программные компоненты взаимодействуют друг с другом посредством API. 
При этом обычно компоненты образуют иерархию — высокоуровневые компоненты 
используют API низкоуровневых компонентов, а те, в свою очередь, 
используют API ещё более низкоуровневых компонентов.
***
>Swagger - это интерактивная документация на базе спецификации **OpenApi** 

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

### dependency injections