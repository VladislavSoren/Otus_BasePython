from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash,
)

from models import db, PostProj
from .forms.post import PostProjForm

posts_app = Blueprint("posts_app", __name__)


@posts_app.get("/", endpoint="list")
def get_products_list():
    products: list[PostProj] = PostProj.query.order_by(PostProj.id).all()
    return render_template(
        "posts/list.html",
        products=products,
        # class_name=PostProj.__name__
        class_name='Post'
    )


def get_product_by_id(product_id: int) -> PostProj:
    return PostProj.query.get_or_404(
        product_id,
        description=f"PostProj {product_id} not found"
    )


@posts_app.get("/<int:product_id>/", endpoint="details")
def get_product_details(product_id: int):
    private_names = [
        '_sa_instance_state',
        'user_id',
        'id',
        'title',
    ]

    product = get_product_by_id(product_id=product_id)
    return render_template(
        "posts/details.html",
        class_name='Post',
        product=product,
        private_names=private_names,
    )


# @posts_app.get("/<int:product_id>/", endpoint="details")
# def get_all_posts_of_user(product_id: int):


@posts_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def create_new_product():
    form = PostProjForm()
    if request.method == "GET":
        return render_template("posts/add.html", form=form)

    if not form.validate_on_submit():  # если НЕ подтверждено при отправке
        return render_template("posts/add.html", form=form), 400

    product = PostProj(
        user_id=form.data['user_id'],
        title=form.data['title'],
        body=form.data['body'],
        proj_name=form.data['proj_name'],
        description=form.data['description'],
        url=form.data['url'],
        other_contributors=form.data['other_contributors'],
    )
    db.session.add(product)
    db.session.commit()
    url = url_for("posts_app.details", product_id=product.id)
    flash(f"Created {PostProj.__name__} {product.title!r}", category="success")
    return redirect(url)


@posts_app.route(
    "/<int:product_id>/confirm-delete/",
    methods=["GET", "POST"],
    endpoint="confirm-delete",
)
def confirm_delete_product(product_id: int):
    product = get_product_by_id(product_id=product_id)
    if request.method == "GET":
        return render_template("posts/confirm-delete.html", product=product)

    product_name = product.title
    db.session.delete(product)
    db.session.commit()
    # Перенаправляемся на страницу с перечнем товара
    flash(f"Deleted {PostProj.__name__} {product_name!r}", category="warning")
    url = url_for("posts_app.list")
    return redirect(url)
