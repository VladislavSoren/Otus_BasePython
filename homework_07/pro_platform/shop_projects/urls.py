from django.urls import path

from .views import shop_index, categories_with_products_tree

app_name = "app_shop_projects"

urlpatterns = [
    path('', shop_index, name="index"),
    path('cats_with_projs', categories_with_products_tree, name="categories_with_products_tree"),
]
