from django.contrib.auth.views import (
    LoginView as LoginViewGeneric,
    LogoutView as LogoutViewGeneric,
)
from django.shortcuts import render
from django.urls import reverse_lazy

from auth_block.forms import AuthenticationForm


class LoginView(LoginViewGeneric):
    template_name = "auth_block/login.html"
    form_class = AuthenticationForm
    next_page = reverse_lazy("auth_block:about-me")


class LogoutView(LogoutViewGeneric):
    next_page = reverse_lazy("auth_block:about-me")
