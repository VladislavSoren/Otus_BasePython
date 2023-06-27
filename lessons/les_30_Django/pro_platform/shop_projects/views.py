from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Project


def shop_index(request: HttpRequest) -> HttpResponse:
    projects = Project.objects.order_by("id").all()

    return render(
        request=request,
        template_name="shop_projects/index.html",
        context={
            "projects": projects,
        }
    )
