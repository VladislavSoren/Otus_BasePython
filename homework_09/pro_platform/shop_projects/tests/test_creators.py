import re

from django.test import TestCase
from django.urls import reverse

from pro_platform.fake import fake
from shop_projects.factories import CreatorFactory, ProjectFactoryBasedDB, CategoryFactory
from shop_projects.models import Creator, Category, Project


class TestCreatorTestCase(TestCase):

    # creation of object
    @classmethod
    def setUpClass(cls):
        # scope on other methods
        cls.creator = CreatorFactory.create()
        # cls.creator_for_default_category = CreatorFactory.create()
        # cls.category = CategoryFactory.create()

        print(Creator.objects.all())
        print(Category.objects.all())
        print(Project.objects.all())

        cls.nb_project = fake.pyint(min_value=2, max_value=7)
        print(cls.nb_project)
        cls.projects = ProjectFactoryBasedDB.create_batch(cls.nb_project)
        # cls.project = ProjectFactoryBasedDB.create()

        print(Project.objects.all())

    # removal of object
    @classmethod
    def tearDownClass(cls):
        # for project in cls.projects:
        #     project.delete()
        cls.project.delete()
        # cls.category.delete()
        cls.creator.delete()
        # cls.creator_for_default_category.delete()

    # checking creation of object
    def test_get_creator(self):
        qs = Creator.objects
        count = qs.count()
        self.assertEqual(count, 1)
        creator = qs.first()
        self.assertEqual(creator.pk, self.creator.pk)

    # checking displaying of object
    def test_get_creator_details(self):
        # url = reverse("shop_projects:creator-details", kwargs={"pk": self.creator.pk})
        url = reverse("shop_projects:creator-details", kwargs={"pk": self.creator.pk})
        response = self.client.get(url)

        ###################
        # checking content
        ###################
        self.assertTemplateUsed(response, "shop_projects/creator_detail.html")
        self.assertContains(response, self.creator.pk)
        self.assertContains(response, self.creator.user)
        self.assertContains(response, self.creator.rating)
        creator_qs = (
            Creator
            .objects
            # .filter(id=self.creator.pk)
            .filter(id=self.creator.pk)
            .prefetch_related("projects_for_creators")
            .first()
        )
        print(creator_qs, creator_qs.projects_for_creators.all())

        ###################
        # checking content
        ###################
        self.assertQuerySetEqual(
            qs=[project.pk for project in creator_qs.projects_for_creators.all()],
            values=(p.pk for p in response.context["object"].projects_for_creators.all()),
        )

        # #######################################
        # # checking refs (active functionality)
        # #######################################
        # # receiving  html of response as str
        # response_content: bytes = response.content
        # response_content_str: str = response_content.decode()
        #
        # # check availability "Update" creator
        # update_ref = f'/shop_projects/creators/{self.creator.pk}/update/'
        # count = len(re.findall(f'href="{update_ref}"', response_content_str))
        # self.assertEqual(count, 1)
        #
        # # check availability "Archive" creator
        # archive_ref = f'/shop_projects/creators/{self.creator.pk}/confirm-delete/'
        # count = len(re.findall(f'href="{archive_ref}"', response_content_str))
        # self.assertEqual(count, 1)
        #
        # # check availability back to all creators (navbar and button)
        # archive_ref = f'/shop_projects/creators'
        # count = len(re.findall(f'href="{archive_ref}"', response_content_str))
        # self.assertEqual(count, 2)

# 
# class ProjectsListViewTestCase(TestCase):
#     # instead of factory we use fixtures (take a lot of time)
#     fixtures = [
#         "users.json",
#         "creators.json",
#         "categories.json",
#         "projects.json",
# 
#     ]
# 
#     def test_get_projects_list(self):
#         url = reverse("shop_projects:projects")
#         response = self.client.get(url)
# 
#         ##########################
#         # checking right template
#         ##########################
#         self.assertTemplateUsed(response, "shop_projects/project_list.html")
# 
#         projects_qs = (
#             Project
#             .objects
#             .filter(status=Project.Status.AVAILABLE)
#             .order_by("id")
#             .only("id")
#             .all()
#         )
# 
#         ###################
#         # checking content
#         ###################
#         self.assertQuerySetEqual(
#             qs=[project.pk for project in projects_qs],
#             values=(p.pk for p in response.context["object_list"]),
#         )
# 
#         #######################################
#         # checking refs (active functionality)
#         #######################################
#         # receiving  html of response as str
#         response_content: bytes = response.content
#         response_content_str: str = response_content.decode()
# 
#         # check availability "create" (navbar and button)
#         count = len(re.findall(r'href="/shop_projects/projects/create/"', response_content_str))
#         self.assertEqual(count, 2)
# 
#         # check availability "back to index" ref (button)
#         count = len(re.findall(r'href="/shop_projects/"', response_content_str))
#         self.assertEqual(count, 1)
