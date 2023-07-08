from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Sum

from shop_projects.models import Order


class OrdersListView(ListView):
    # queryset = (
    #     Order
    #     .objects
    #     .filter(status=Order.Status.AVAILABLE)
    #     .order_by("id")
    #     .prefetch_related("user", "projects")
    #     .defer(
    #         "promocode",
    #         "created_at",
    #         "updated_at",
    #     )
    #     .all()
    # )

    queryset = (
        Order
        .objects
        .filter(status=Order.Status.AVAILABLE)
        .order_by("id")
        .prefetch_related("projects")
        .values('id')
        .annotate(Sum('projects__price'))
    )

    queryset_aggr_proj_sum = (
        Order
        .objects
        .filter(status=Order.Status.AVAILABLE)
        .order_by("id")
        .prefetch_related("user", "projects")
        .defer(
            "promocode",
            "created_at",
            "updated_at",
        )
        .all()
    )

    # queryset_aggr_proj_sum

    extra_context = {
        "categories": queryset,
        "class_name": Order._meta.object_name.lower(),
        "class_name_plural": Order._meta.verbose_name_plural,
        "orders_projs_sum": queryset_aggr_proj_sum,
    }

    # queryset_aggr_proj_sum[0]['projects__price__sum']


def order_list_view(request: HttpRequest) -> HttpResponse:
    query_orders = (
        Order
        .objects
        .filter(status=Order.Status.AVAILABLE)
        .order_by("id")
        .prefetch_related("user")
        .defer(
            "promocode",
            "created_at",
            "updated_at",
        )
        .all()
    )

    query_aggr_proj_sum = (
        Order
        .objects
        .filter(status=Order.Status.AVAILABLE)
        .order_by("id")
        .prefetch_related("projects")
        .values('id')
        .annotate(Sum('projects__price'))
    )

    query_list = zip(query_orders, query_aggr_proj_sum)

    return render(
        request=request,
        template_name="shop_projects/order_list.html",
        context={
            "query_list": query_list,
            "class_name": Order._meta.object_name.lower(),
            "class_name_plural": Order._meta.verbose_name_plural,
        }
    )


def order_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    queryset = (
        Order
        .objects
        .filter(id=pk)
        .prefetch_related("user", "projects")
        .all()
    )

    query_aggr_proj_sum = (
        Order
        .objects
        .filter(id=pk)
        .filter(status=Order.Status.AVAILABLE)
        .prefetch_related("projects")
        .values('id')
        .annotate(Sum('projects__price'))
    )

    query_list = zip(queryset, query_aggr_proj_sum)

    return render(
        request=request,
        template_name="shop_projects/order_detail.html",
        context={
            "query_list": query_list,
            "class_name": Order._meta.object_name.lower(),
            "class_name_plural": Order._meta.verbose_name_plural,
            "back_url_to_all_objs": 'shop_projects:orders',
        }
    )


# class ProjectCreateView(CreateView):
#     model = Project
#     form_class = ProjectForm
#     success_url = reverse_lazy("shop_projects:projects")
#
#     extra_context = {
#         "class_name": Project._meta.object_name.lower(),
#         "class_name_plural": Project._meta.verbose_name_plural,
    }
#
#
# class ProjectUpdateView(UpdateView):
#     template_name_suffix = "_update_form"
#     model = Project
#     form_class = ProjectForm
#
#     extra_context = {
#         "class_name": Project._meta.object_name.lower(),
#         "class_name_plural": Project._meta.verbose_name_plural,
#     }
#
#     def get_success_url(self):
#         return reverse(
#             "shop_projects:project-details",
#             kwargs={
#                 "pk": self.object.pk,
#             }
#         )
#
#
# class ProjectDeleteView(DeleteView):
#     success_url = reverse_lazy("shop_projects:projects")
#     queryset = (
#         Project
#         .objects
#         .filter(status=Project.Status.AVAILABLE)
#         .all()
#     )
#
#     def form_valid(self, form):
#         success_url = self.get_success_url()
#         self.object.status = Project.Status.ARCHIVED
#         self.object.save()
#         return redirect(success_url)
