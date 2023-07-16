from django.test import TestCase
from django.urls import reverse

from shop_projects.models import Project


class ProjectsListViewTestCase(TestCase):
    fixtures = [
        "cat-fix.json",
        "creat-fix.json",
        "proj-fix.json",
        "user-fix.json",
    ]

    def test_ok(self):
        url = reverse("shop_projects:projects")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "shop_projects/project_list.html")

        projects_qs = (
            Project
            .objects
            .filter(status=Project.Status.AVAILABLE)
            .order_by("id")
            .only("id")
            .all()
        )

        self.assertQuerySetEqual(
            # qs=projects_qs,
            # values=(p.pk for p in response.context["object_list"]),  # values to we expect to see
            # transform=lambda p: p.pk,

            qs=[project.pk for project in projects_qs],
            values=(p.pk for p in response.context["object_list"]),
        )
