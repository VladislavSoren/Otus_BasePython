from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash,
)

from models import db, User
from .forms.users import UserForm

users_app = Blueprint("users_app", __name__)


@users_app.get("/", endpoint="list")
def get_products_list():
    products: list[User] = User.query.order_by(User.id).all()
    return render_template("users/list.html", products=products)


def get_product_by_id(product_id: int) -> User:
    return User.query.get_or_404(
        product_id,
        description=f"User {product_id} not found"
    )


@users_app.get("/<int:product_id>/", endpoint="details")
def get_product_details(product_id: int):
    product = get_product_by_id(product_id=product_id)
    return render_template("users/details.html", product=product)


@users_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def create_new_product():
    form = UserForm()
    if request.method == "GET":
        return render_template("users/add.html", form=form)

    if not form.validate_on_submit():  # если НЕ подтверждено при отправке
        return render_template("users/add.html", form=form), 400

    product = User(name=form.data['name'], username=form.data['username'])
    db.session.add(product)
    db.session.commit()
    url = url_for("users_app.details", product_id=product.id)
    flash(f"Created {User.__name__} {product.name!r}", category="success")
    return redirect(url)


@users_app.route(
    "/<int:product_id>/confirm-delete/",
    methods=["GET", "POST"],
    endpoint="confirm-delete",
)
def confirm_delete_product(product_id: int):
    product = get_product_by_id(product_id=product_id)
    if request.method == "GET":
        return render_template("users/confirm-delete.html", product=product)

    product_name = product.name
    db.session.delete(product)
    db.session.commit()
    # Перенаправляемся на страницу с перечнем товара
    flash(f"Deleted {User.__name__} {product_name!r}", category="warning")
    url = url_for("users_app.list")
    return redirect(url)
