from flask import Blueprint

items_app = Blueprint("items_app", __name__)


@items_app.get("/")
def items_list():
    return {
        "data": [
            {
                "id": 1,
                "name": "abc",
            },
            {
                "id": 2,
                "name": "qwe",
            },
        ]
    }


@items_app.get("/<int:item_id>/")
def items_list_from_path(item_id: int):
    return {
        "data": [
            {
                "id": item_id,
                "name": "abc",
            },
        ]
    }


@items_app.post("/")
def create_item():
    return {

    }