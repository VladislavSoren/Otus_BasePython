from flask import Blueprint, render_template

items_app = Blueprint("items_app", __name__)


@items_app.get("/", endpoint="list")
def items_list():
    return render_template("items/list.html")


@items_app.get("/<int:item_id>/", endpoint="details")
def item_details(item_id: int):
    return {
        "data": {
            "id": item_id,
            "name": "single",
        }
    }


@items_app.post("/")
def create_item():
    return {

    }
