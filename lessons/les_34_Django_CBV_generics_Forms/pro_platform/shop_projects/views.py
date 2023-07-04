from celery.result import AsyncResult
from django.db.models import Q
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from shop_projects.tasks import notify_order_saved
from .forms import CategoryForm
from .models import (
    Project,
    Category,
    Order,
)


class CategoryListView(ListView):
    # model = Category
    queryset = (
        Category
        .objects
        .filter(~Q(archived=True))
        .all()
    )


class CategoryDetailView(DetailView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    # fields = "name", "description",
    # success_url = reverse  #
    success_url = reverse_lazy("shop_projects:categories")


class CategoryUpdateView(UpdateView):
    template_name_suffix = "_update_form"
    model = Category
    form_class = CategoryForm

    # fields = "description",
    # success_url = reverse_lazy("shop_projects:category", {})

    def get_success_url(self):
        return reverse(
            "shop_projects:category",
            kwargs={
                "pk": self.object.pk,
            }
        )


class CategoryDeleteView(DeleteView):
    # model = Category
    success_url = reverse_lazy("shop_projects:categories")
    queryset = (
        Category
        .objects
        .filter(~Q(archived=True))
        .all()
    )

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        # return HttpResponseRedirect(success_url)
        return redirect(success_url)


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
