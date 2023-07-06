from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from shop_projects.models import Donat


def donats_view(request: HttpRequest) -> HttpResponse:
    donats = (
        Donat
        .objects
        .order_by("id")
        .select_related("user")
        .prefetch_related("projects")
        .all()
    )

    return render(
        request=request,
        template_name="shop_projects/donats.html",
        context={
            "donats": donats,
        }
    )