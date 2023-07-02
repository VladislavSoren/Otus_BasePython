from django.urls import path

from .views import shop_index, categories_with_products_tree, projects_view, orders_view

app_name = "shop_projects"

urlpatterns = [
    path('', shop_index, name="index"),
    path('projects/', projects_view, name="projects"),
    path("orders/", orders_view, name="orders"),
    path('cats_with_projs/', categories_with_products_tree, name="categories_with_products_tree"),
]
