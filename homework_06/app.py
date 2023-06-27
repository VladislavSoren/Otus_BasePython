from os import getenv

from flask import Flask, request, render_template
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from models import db
from views.users import users_app
from views.items import items_app
from views.posts import posts_app

app = Flask(__name__)
app.register_blueprint(items_app, url_prefix="/items")
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(posts_app, url_prefix="/posts")

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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
