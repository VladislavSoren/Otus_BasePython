`WSGI` (Web Server Gateway Interface) — стандарт взаимодействия между Python-программой, 
выполняющейся на стороне сервера, и самим веб-сервером, например Apache.

Эволюция упрощения:
Чистый `WSGI` -> `Werkzeug` -> `Flask`

Notes:
- http://127.0.0.1:5000/hello/?name=Vlad (передача параметра в запросе)
- В режиме Debugger можно через терминал в браузере управлять проектом,
поэтому НЕЛЬЗЯ допускать дебаг режим в прод!
- Blueprint - аналог router из FastAPI
- Зависимости как в FastAPI нельзя сделать
- json это не обязательно словарь, это может быть почти любой объект
- details.html and list.html - наследники шаблона base.html,
их содержимое заменяет блоки в base

Fails:
- Видимо из-за этой фигни: `WARNING: This is a development server. Do not use it in a production deployment. 
Use a production WSGI server instead.` - падает предсказание ЗП
- В комьюнити НЕТ никакой джинжи, которая подсказывать как писать дич в html файлах

To Do List:
- Frontend для FastAPI