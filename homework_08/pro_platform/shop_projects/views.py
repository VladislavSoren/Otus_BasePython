from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ProjectForm
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
        .filter(status=Project.Status.AVAILABLE)
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
        "class_name": Project._meta.object_name.lower(),
        "class_name_plural": Project._meta.verbose_name_plural,
    }


class ProjectDetailView(DetailView):
    queryset = (
        Project
        .objects
        .order_by("id")
        .select_related("creator")
        .prefetch_related("donats", "donats__user")
        .all()
    )

    extra_context = {
        "categories": queryset,
        "class_name": Project._meta.object_name.lower(),
        "class_name_plural": Project._meta.verbose_name_plural,
        "back_url_to_all_objs": 'shop_projects:projects',
    }


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("shop_projects:projects")

    extra_context = {
        "class_name": Project._meta.object_name.lower(),
        "class_name_plural": Project._meta.verbose_name_plural,
    }


class ProjectUpdateView(UpdateView):
    template_name_suffix = "_update_form"
    model = Project
    form_class = ProjectForm

    extra_context = {
        "class_name": Project._meta.object_name.lower(),
        "class_name_plural": Project._meta.verbose_name_plural,
    }

    def get_success_url(self):
        return reverse(
            "shop_projects:project-details",
            kwargs={
                "pk": self.object.pk,
            }
        )


class ProjectDeleteView(DeleteView):
    success_url = reverse_lazy("shop_projects:projects")
    queryset = (
        Project
        .objects
        .filter(status=Project.Status.AVAILABLE)
        .all()
    )

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.status = Project.Status.ARCHIVED # .value
        self.object.save()
        # return HttpResponseRedirect(success_url)
        return redirect(success_url)


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
