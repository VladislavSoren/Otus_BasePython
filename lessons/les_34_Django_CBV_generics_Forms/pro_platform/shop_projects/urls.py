from django.urls import path

from .views import (
    ShopIndexView,
    CategoriesWithProductsTree,
    ProjectsView,
    OrdersListView,
    get_task_info,
    CategoryListView,
    CategoryCreateView,
    CategoryDetailView,
    CategoryUpdateView,
    CategoryDeleteView,
)

app_name = "shop_projects"

urlpatterns = [
    path('', ShopIndexView.as_view(), name="index"),
    path('projects/', ProjectsView.as_view(), name="projects"),
    path("orders/", OrdersListView.as_view(), name="orders"),
    path("orders/task/<task_id>/", get_task_info, name="get-order-task-id"),

    path("categories/", CategoryListView.as_view(), name="categories"),
    path("categories/create/", CategoryCreateView.as_view(), name="create-category"),


    path("categories/<int:pk>/update/", CategoryUpdateView.as_view(), name="update-category"),
    path("categories/<int:pk>/confirm-delete/", CategoryDeleteView.as_view(), name="confirm-delete-category"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category"),



    path('cats_with_projs/', CategoriesWithProductsTree.as_view(), name="categories_with_products_tree"),

]
