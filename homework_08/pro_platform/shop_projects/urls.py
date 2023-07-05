from django.urls import path

from .views import (
    ShopIndexView,

    ProjectsListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,

    categories_with_products_tree,
    creators_with_products_tree,
    donats_view,

)

app_name = "shop_projects"

urlpatterns = [
    path('', ShopIndexView.as_view(), name="index"),
    path('projects', ProjectsListView.as_view(), name="projects"),
    path("projects/create/", ProjectCreateView.as_view(), name="create-project"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-details"),

    path("projects/<int:pk>/update/", ProjectUpdateView.as_view(), name="update-project"),
    path("projects/<int:pk>/confirm-delete/", ProjectDeleteView.as_view(), name="confirm-delete-project"),




    path('cats_with_projs', categories_with_products_tree, name="categories_with_products_tree"),
    path('creators_with_projs', creators_with_products_tree, name="creators_with_products"),
    path('donats', donats_view, name="donats"),

]
