from celery.result import AsyncResult
from django.db.models import Q
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
)

from shop_projects.tasks import notify_order_saved
from .forms import CategoryForm
from .models import (
    Project,
    Category,
    Order,
)


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    # fields = "name", "description",
    # success_url = reverse  #
    success_url = reverse_lazy("shop_projects:categories")


class ShopIndexView(TemplateView):
    template_name = "shop_projects/index.html"


class ProjectsView(View):
    template_name = "shop_projects/projects.html"

    def get(self, request: HttpRequest) -> HttpResponse:
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
            template_name=self.template_name,
            context={
                "projects": projects,
            },
        )


class OrdersListView(ListView):
    template_name = "shop_projects/orders.html"
    context_object_name = "orders"
    queryset = (
        Order
        .objects
        .order_by("id")
        # to one
        .select_related("user", "payment_details")
        # to many
        .prefetch_related("projects")
        .all()
    )


class CategoriesWithProductsTree(TemplateView):
    template_name = "shop_projects/categories-with-projects-tree.html"

    extra_context = {
        "categories": Category.objects.order_by("id").prefetch_related('projects').all()
    }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     categories = Category.objects.order_by("id").prefetch_related('projects').all()
    #     context.update(categories=categories)
    #     return context


def get_task_info(request: HttpRequest, task_id: str) -> HttpResponse:
    task_result: AsyncResult = notify_order_saved.AsyncResult(task_id)

    return JsonResponse({
        "task_id": task_result.id,
        "task_status": task_result.status,
        "name": task_result.name,
        # "backend": str(task_result.backend),
    })
