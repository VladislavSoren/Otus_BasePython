from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import (
    Project,
    Category,
    Creator,
    Donat,
)


# @register.filter
# def to_class_name(value):
#     return value.__class__.__name__


class ShopIndexView(TemplateView):
    template_name = "shop_projects/index.html"


class ProjectsListView(ListView):
    queryset = (
        Project
        .objects
        .filter(~Q(status=Project.Status.ARCHIVED))
        .order_by("id")
        .select_related("category")
        .defer(
            "description",
            "created_at",
            "updated_at",
            "category__description",
        )
        .all()
    )

    extra_context = {
        "categories": queryset,
        "class_name": Project._meta.object_name,
        "class_name_plural": Project._meta.verbose_name_plural,
    }


class ProjectDetailView(DetailView):

    queryset = (
        Project
        .objects
        .order_by("id")
        .select_related("creator")
        .prefetch_related("donats")
        .all()
    )

    extra_context = {
        "categories": queryset,
        "class_name": Project._meta.object_name,
        "class_name_plural": Project._meta.verbose_name_plural,
    }


def projects_with_donats(request: HttpRequest) -> HttpResponse:
    projects = (
        Project
        .objects
        .order_by("id")
        .select_related("creator")
        .prefetch_related("donats", "donats__user")
        .all()
    )

    return render(
        request=request,
        template_name="shop_projects/projects_with_donats.html",
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



