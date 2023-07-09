
from django.urls import path, include
from django.views.generic import TemplateView

from .views import (
    LoginView,
    LogoutView,
)

app_name = "auth_block"

urlpatterns = [
    path(
        "login/",
        # TemplateView.as_view(template_name="auth_block/login.html"),
        LoginView.as_view(),
        name="login"
    ),

    path(
        "logout/",
        # TemplateView.as_view(template_name="auth_block/login.html"),
        LogoutView.as_view(),
        name="logout"
    ),

    path("me/", TemplateView.as_view(template_name="auth_block/me.html"), name="about-me"),
]

