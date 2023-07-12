from django.urls import path, include
from django.views.generic import TemplateView

from my_projects.views.image_sex_age_view import (
    image_request
)

app_name = "my_projects"

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="my_projects/index.html"),
        name="index"
    ),

    path(
        "sex_age_humans_detection/",
        image_request,
        name="sex_age_detection"
    ),

]
