from django.urls import path

from .views import (
    ShopIndexView,

    ProjectsListView,
    ProjectDetailView,

    categories_with_products_tree,
    creators_with_products_tree,
    donats_view,
    projects_with_donats,
)

app_name = "shop_projects"

urlpatterns = [
    path('', ShopIndexView.as_view(), name="index"),
    path('projects', ProjectsListView.as_view(), name="projects"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-details"),



    path('cats_with_projs', categories_with_products_tree, name="categories_with_products_tree"),
    path('creators_with_projs', creators_with_products_tree, name="creators_with_products"),
    path('donats', donats_view, name="donats"),
    path('projects_with_donats', projects_with_donats, name="projects_with_donats"),
]
