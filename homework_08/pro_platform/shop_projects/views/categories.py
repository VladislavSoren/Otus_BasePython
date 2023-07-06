from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from shop_projects.forms import CategoryForm
from shop_projects.models import Category


class CategoriesListView(ListView):
    queryset = (
        Category
        .objects
        .filter(status=Category.Status.AVAILABLE)
        .order_by("id")
        .all()
    )

    extra_context = {
        "categories": queryset,
        "class_name": Category._meta.object_name.lower(),
        "class_name_plural": Category._meta.verbose_name_plural,
    }


class CategoryDetailView(DetailView):
    queryset = (
        Category
        .objects
        .order_by("id")
        .prefetch_related("projects_for_cats")
        .all()
    )

    extra_context = {
        "categories": queryset,
        "class_name": Category._meta.object_name.lower(),
        "class_name_plural": Category._meta.verbose_name_plural,
        "back_url_to_all_objs": 'shop_projects:categories',
    }


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("shop_projects:categories")

    extra_context = {
        "class_name": Category._meta.object_name.lower(),
        "class_name_plural": Category._meta.verbose_name_plural,
    }


class CategoryUpdateView(UpdateView):
    template_name_suffix = "_update_form"
    model = Category
    form_class = CategoryForm

    extra_context = {
        "class_name": Category._meta.object_name.lower(),
        "class_name_plural": Category._meta.verbose_name_plural,
    }

    def get_success_url(self):
        return reverse(
            "shop_projects:category-details",
            kwargs={
                "pk": self.object.pk,
            }
        )


class CategoryDeleteView(DeleteView):
    success_url = reverse_lazy("shop_projects:categories")
    queryset = (
        Category
        .objects
        .filter(status=Category.Status.AVAILABLE)
        .all()
    )

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.status = Category.Status.ARCHIVED  # .value
        self.object.save()
        return redirect(success_url)
