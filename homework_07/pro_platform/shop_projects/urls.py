from django.urls import path

from .views import shop_index, categories_with_products_tree, creators_with_products_tree

app_name = "shop_projects"

urlpatterns = [
    path('', shop_index, name="index"),
    path('cats_with_projs', categories_with_products_tree, name="categories_with_products_tree"),
    path('creators_with_projs', creators_with_products_tree, name="creators_with_products"),
]
