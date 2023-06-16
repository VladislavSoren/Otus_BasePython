from flask import Flask, request

from views.products import products_app
from views.items import items_app

app = Flask(__name__)
app.register_blueprint(items_app, url_prefix="/items")
app.register_blueprint(products_app, url_prefix="/products")

@app.get("/")
def hello_root():
    print(request.args)
    return "Hello World!"


# /hello и /hello/ - два разных адреса!
# @app.get("/hello/")
def hello():
    # http://127.0.0.1:5000/hello/?spam=egs&foo=1&foo=2
    print(request.args)
    print(request.args.get("spam"))
    print(request.args.get("foo"))
    print(request.args.getlist("foo"))

    name = request.args.get("name")
    if not name:
        name = "World"
    else:
        name.strip()
    return f"Hello {name}!"


# @app.get("/hello/<name>/")
# def hello_path(name: str):
#     if not name:
#         name = "World"
#     else:
#         name.strip()
#     return f"Hello {name}!"


@app.get("/hello/")  # two
@app.get("/hello/<name>/")  # one
def hello_path(name: str | None = None):
    if name is None:
        name = request.args.get("name", "")  # если НИЧЕГО не нашли -> ""
    name = name.strip()
    if not name:  # альтернатива if name == ""
        name = "World"
    return f"Hello {name}!"




if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
