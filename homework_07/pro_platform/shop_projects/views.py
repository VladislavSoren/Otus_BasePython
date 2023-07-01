from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import (
    Project,
    Category,
    Creator,
    Donat,
)




def shop_index(request: HttpRequest) -> HttpResponse:
    '''
    select_related - к одному (как joinedload в алхимии )
    prefetch_related - ко многим
    '''
    projects = (
        Project
        .objects
        .filter(~Q(status=Project.Status.ARCHIVED))
        .order_by("id")
        .select_related('category')
        .defer(
            "created_at",
            "updated_at",
            "category__description")  # __ == .
        .all()
    )

    return render(
        request=request,
        template_name="shop_projects/index.html",
        context={
            "projects": projects,
        }
    )


def categories_with_products_tree(request: HttpRequest) -> HttpResponse:
    # Пока к categories не обратились, запросов в БД НЕ будет
    categories = Category.objects.order_by("id").prefetch_related('projects_for_cats').all()  #

    return render(
        request=request,
        template_name="shop_projects/categories-with-projects-tree.html",
        context={
            "categories": categories,
        }
    )


def creators_with_products_tree(request: HttpRequest) -> HttpResponse:
    # Пока к categories не обратились, запросов в БД НЕ будет
    creators = Creator.objects.order_by("id").prefetch_related('projects_for_creators').all()  #

    return render(
        request=request,
        template_name="shop_projects/creators-with-projects.html",
        context={
            "creators": creators,
        }
    )


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


def projects_with_donats(request: HttpRequest) -> HttpResponse:
    projects = (
        Project
        .objects
        .order_by("id")
        .select_related("creator")
        .prefetch_related("donats")
        .all()
    )

    return render(
        request=request,
        template_name="shop_projects/projects_with_donats.html",
        context={
            "projects": projects,
        }
    )