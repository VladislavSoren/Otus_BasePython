## http запрос 


Методы позволяют передавать данные в различном виде

#### GET:
* The GET method requests a representation of the specified resource. 
Requests using GET should only retrieve data.
* Метод GET запрашивает представление ресурса. 
Запросы с использованием этого метода могут только извлекать данные.
#### Свойства:
- Safe (Безопасный метод это тот, который не изменяет ресурс с которым работаем)
- Idempotent: True
***

#### POST:
* The POST method submits an entity to the specified resource, 
often causing a change in state or side effects on the server.
* POST используется для отправки сущностей к определённому ресурсу. 
Часто вызывает изменение состояния или какие-то побочные эффекты на сервере.
#### Свойства:
- Unsafe, т.е. нужно проводить дополнительные проверки
- Не обязательно только изменяет, но и получает данные
- Нужен для создания какой-либо сущности
- Idempotent: False
***

#### DELETE:
* The DELETE method deletes the specified resource.
* DELETE удаляет указанный ресурс.
#### Свойства:
- Safe: False
- Idempotent: True
***

#### PUT:
* The PUT method replaces all current representations of the target resource 
with the request payload.
* PUT заменяет все текущие представления ресурса данными запроса.
Заменяет запись ЦЕЛИКОМ!
#### Свойства:
- Safe: False
- Idempotent: True
> Метод PATCH в отличие от PUT может ЧАСТИЧНО изменять ресурс, поэтому
он Unsafe 


HTTP-метод является идемпотентным, 
если ожидаемое воздействие на сервер от выполнения одного запроса такое же, 
как и от выполнения нескольких идентичных запросов.
При ПОВТОРНОМ запросе МЕТОД НИЧЕГО НЕ МЕНЯЕТ!
>!Поэтому delete идемпотентный.
***

### Есть несколько мест, где мы можем передавать информацию:
- Адресная строка (не используется для передачи секретных данных)
- Заголовки (передаётся доп информация, location, авторизация и т.п.)
- Тело
***

### Статусы
- HTTP response status codes indicate whether a specific HTTP request has been successfully completed. 
Responses are grouped in five classes:
- Код ответа (состояния) HTTP показывает, был ли успешно выполнен определённый HTTP запрос. 
Коды сгруппированы в 5 классов:
  * Informational responses (100 – 199)
  * Successful responses (200 – 299)
  * Redirection messages (300 – 399)
  * Client error responses (400 – 499), юзер допустил ошибку и сервер это понял
  * Server error responses (500 – 599), ошибка на сервере или косяк юзера не понят

### WSGI (Web Server Gateway Interface):
стандарт (протокол) взаимодействия между Python-программой, выполняющейся на стороне сервера, 
и самим веб-сервером[1], например Apache.

gunicorn:
«Green Unicorn» — это HTTP-сервер с интерфейсом шлюза веб-сервера Python. 

### Заметки:
- Иногда может возвращаться ответ со статусом 200, но внутри
будет ошибка, это зашквар, но такое встречается
- HTML forms
- Тело запроса
