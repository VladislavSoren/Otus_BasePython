from django.views.generic import ListView, DetailView

from shop_projects.models import Creator


class CreatorsListView(ListView):
    queryset = (
        Creator
        .objects
        .filter(status=Creator.Status.AVAILABLE)
        .select_related("user")
        .order_by("id")
        .all()
    )

    extra_context = {
        "categories": queryset,
        "class_name": Creator._meta.object_name.lower(),
        "class_name_plural": Creator._meta.verbose_name_plural,
    }


class CreatorDetailView(DetailView):
    queryset = (
        Creator
        .objects
        .order_by("id")
        .select_related("user")
        .prefetch_related("projects_for_creators")
        .all()
    )

    extra_context = {
        "categories": queryset,
        "class_name": Creator._meta.object_name.lower(),
        "class_name_plural": Creator._meta.verbose_name_plural,
        "back_url_to_all_objs": 'shop_projects:creators',
    }

#
#
# class ProjectCreateView(CreateView):
#     model = Project
#     form_class = ProjectForm
#     success_url = reverse_lazy("shop_projects:projects")
#
#     extra_context = {
#         "class_name": Project._meta.object_name.lower(),
#         "class_name_plural": Project._meta.verbose_name_plural,
#     }
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
#         self.object.status = Project.Status.ARCHIVED  # .value
#         self.object.save()
#         # return HttpResponseRedirect(success_url)
#         return redirect(success_url)
