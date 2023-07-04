from celery.result import AsyncResult
from django.db.models import Q
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render

from shop_projects.tasks import notify_order_saved
from .models import Project, Category, Order

Q


def shop_index(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name="shop_projects/index.html",
        context={},
    )


def projects_view(request: HttpRequest) -> HttpResponse:
    projects = (
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

    return render(
        request=request,
        template_name="shop_projects/projects.html",
        context={
            "projects": projects,
        },
    )


def orders_view(request: HttpRequest) -> HttpResponse:
    # нагибаем N+N+1! с помощью select_related и prefetch_related
    orders = (
        Order
        .objects
        .order_by("id")
        # to one
        .select_related("user", "payment_details")
        # to many
        .prefetch_related("projects")
        # all objects
        .all()
    )

    return render(
        request=request,
        template_name="shop_projects/orders.html",
        context={
            "orders": orders,
        }
    )


def categories_with_products_tree(request: HttpRequest) -> HttpResponse:
    # Пока к categories не обратились, запросов в БД НЕ будет
    categories = Category.objects.order_by("id").prefetch_related('projects').all()  #

    return render(
        request=request,
        template_name="shop_projects/categories-with-projects-tree.html",
        context={
            "categories": categories,
        }
    )


def get_task_info(request: HttpRequest, task_id: str) -> HttpResponse:
    task_result: AsyncResult = notify_order_saved.AsyncResult(task_id)

    return JsonResponse({
        "task_id": task_result.id,
        "task_status": task_result.status,
        "name": task_result.name,
        # "backend": str(task_result.backend),
    })
