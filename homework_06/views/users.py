from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash,
)
from sqlalchemy.orm import joinedload

from models import db, User, PostProj
from .forms.user import UserForm

users_app = Blueprint("users_app", __name__)


@users_app.get("/", endpoint="list")
def get_products_list():
    products: list[User] = User.query.order_by(User.id).all()

    return render_template(
        "users/list.html",
        products=products,
        # class_name=products[0].__class__.__name__
        class_name=User.__name__
    )


def get_product_by_id(product_id: int) -> User:
    return User.query.get_or_404(
        product_id,
        description=f"User {product_id} not found"
    )


@users_app.get("/<int:product_id>/", endpoint="details")
def get_product_details(product_id: int):
    private_names = [
        '_sa_instance_state',
        # 'email',
        # 'id',  # На проде id НЕ будут доступны
        'posts',  # При вытягивании постов автоматом добавляется в атрибуты
    ]

    # user_with_posts: User = (
    #     User.query
    #     .options(joinedload('posts', innerjoin=True))
    #     .order_by("id")
    #     .filter(User.id == product_id)
    #     .one_or_404()
    # )

    # Способ ниже даёт тот результат, но гораздо короче в записи
    product: User = get_product_by_id(product_id=product_id)
    posts_of_user: list[PostProj] = product.posts

    return render_template(
        "users/details.html",
        class_name=User.__name__,
        product=product,
        private_names=private_names,
        posts=posts_of_user,
    )


@users_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def create_new_product():
    form = UserForm()
    if request.method == "GET":
        return render_template("users/add.html", form=form)

    if not form.validate_on_submit():  # если НЕ подтверждено при отправке
        return render_template("users/add.html", form=form), 400

    product = User(name=form.data['name'],
                   username=form.data['username'],
                   email=form.data['email'],
                   profession_type=form.data['profession_type'],
                   website=form.data['website'],
                   )
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
