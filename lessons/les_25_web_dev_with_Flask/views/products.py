from flask import Blueprint, render_template, request, url_for, redirect

from dataclasses import dataclass, field
from werkzeug.exceptions import NotFound, BadRequest

products_app = Blueprint("products_app", __name__)


@dataclass
class Product:
    id: int
    name: str


@dataclass
class ProductStorage:
    last_id: int = 0
    products: dict[int: Product] = field(default_factory=dict)  # instead of list

    @property
    def next_id(self):
        self.last_id += 1
        return self.last_id

    def add_product(self, name: str):
        product = Product(id=self.next_id, name=name)
        self.products[product.id] = product
        return product

    def delete_product_by_id(self, product_id: int):
        self.products.pop(product_id)
        return "Done"

    def get_all_products(self) -> list[Product]:
        return list(self.products.values())

    def get_product_by_id(self, product_id: int) -> Product | None:
        return self.products.get(product_id)


storage = ProductStorage()

storage.add_product(name='Notebook')
storage.add_product(name='Camera')


@products_app.get("/", endpoint="list")
def get_products_list():
    products: list[Product] = storage.get_all_products()
    return render_template("list.html", products=products)


def get_product_by_id(product_id: int) -> Product:
    product: Product | None = storage.get_product_by_id(product_id)
    if product:
        return product
    raise NotFound(f"Product {product_id} not found")


@products_app.get("/<int:product_id>/", endpoint="details")
def get_product_details(product_id: int):
    product = get_product_by_id(product_id=product_id)
    return render_template("details.html", product=product)


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def create_new_product():
    if request.method == "GET":
        return render_template("add.html")

    button_click_value = request.form.get("add-button", "")

    product_name = request.form.get("product-name", "")
    product_name = product_name.strip()
    if not product_name:
        raise BadRequest("Product name is required!")

    product = storage.add_product(name=product_name)
    url = url_for("products_app.details", product_id=product.id)
    return redirect(url)


@products_app.route(
    "/confirm-delete/<int:product_id>/",
    methods=["GET", "POST"],
    endpoint="confirm-delete",
)
def confirm_delete_product(product_id: int):
    if request.method == "GET":
        product = get_product_by_id(product_id=product_id)
        return render_template("confirm-delete.html", product=product)
    storage.delete_product_by_id(product_id=product_id)

    # Перенаправляемся на страницу с перечнем товара
    url = url_for("products_app.list")
    return redirect(url)
