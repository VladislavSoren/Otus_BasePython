from os import getenv

from flask import Flask, request, render_template
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from models import db
from views.users import users_app
from views.items import items_app

app = Flask(__name__)
app.register_blueprint(items_app, url_prefix="/items")
app.register_blueprint(users_app, url_prefix="/users")

config_class_name = getenv("CONFIG_CLASS", "DevelopmentConfig")
config_object = f'config.{config_class_name}'
app.config.from_object(config_object)

# Initialise db for our app
db.init_app(app)
migrate = Migrate(app=app, db=db)

# Setting csrf protection
csrf = CSRFProtect(app)

@app.get("/", endpoint="index")
def hello_root():
    return render_template("index.html")


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


@app.get("/loading/")  # one
def loading_page():
    return render_template("loading.html")


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
    app.run(host="0.0.0.0", debug=True)
    # app.run()
