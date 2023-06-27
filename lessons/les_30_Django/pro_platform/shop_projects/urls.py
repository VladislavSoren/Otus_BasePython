from django.urls import path

from .views import shop_index

app_name = "app_shop_projects"

urlpatterns = [
    path('', shop_index, name="index")
]
