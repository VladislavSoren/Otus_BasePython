from django.urls import path

from .views.index import ShopIndexView
from .views.projects import (
    ProjectsListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
)
from .views.categories import (
    CategoriesListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)
from .views.creators import (
    CreatorsListView,
    CreatorDetailView,
    CreatorCreateView,
    CreatorUpdateView,
    CreatorDeleteView,
)

# from .views.donats import (
#     DonatsListView,
#     DonatDetailView,
#     DonatCreateView,
#     DonatUpdateView,
#     DonatDeleteView,
# )

app_name = "shop_projects"

urlpatterns = [
    path('', ShopIndexView.as_view(), name="index"),
    
    path('projects', ProjectsListView.as_view(), name="projects"),
    path("projects/create/", ProjectCreateView.as_view(), name="create-project"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-details"),
    path("projects/<int:pk>/update/", ProjectUpdateView.as_view(), name="update-project"),
    path("projects/<int:pk>/confirm-delete/", ProjectDeleteView.as_view(), name="confirm-delete-project"),

    path('categories', CategoriesListView.as_view(), name="categories"),
    path("categories/create/", CategoryCreateView.as_view(), name="create-category"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-details"),
    path("categories/<int:pk>/update/", CategoryUpdateView.as_view(), name="update-category"),
    path("categories/<int:pk>/confirm-delete/", CategoryDeleteView.as_view(), name="confirm-delete-category"),

    path('creators', CreatorsListView.as_view(), name="creators"),
    path("creators/create/", CreatorCreateView.as_view(), name="create-creator"),
    path("creators/<int:pk>/", CreatorDetailView.as_view(), name="creator-details"),
    path("creators/<int:pk>/update/", CreatorUpdateView.as_view(), name="update-creator"),
    path("creators/<int:pk>/confirm-delete/", CreatorDeleteView.as_view(), name="confirm-delete-creator"),





]
