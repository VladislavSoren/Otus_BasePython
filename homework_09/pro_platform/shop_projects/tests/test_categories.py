import re

from django.db.models import Q
from django.test import TestCase
from django.urls import reverse

from pro_platform.fake import fake

from shop_projects.models import Category


class TestCategoryTestCase(TestCase):

    # creation of object
    @classmethod
    def setUpClass(cls):
        from shop_projects.factories.category import CategoryFactory

        # scope on other methods
        cls.category = CategoryFactory.create()

    # removal of object
    @classmethod
    def tearDownClass(cls):
        cls.category.delete()

    # checking creation of object
    def test_get_category(self):
        # Except "default" category
        qs = Category.objects.filter(~Q(name="default"))
        count = qs.count()
        self.assertEqual(count, 1)
        category = qs.first()
        self.assertEqual(category.pk, self.category.pk)

    # checking displaying of object
    def test_get_category_details(self):
        url = reverse("shop_projects:category-details", kwargs={"pk": self.category.pk})
        response = self.client.get(url)

        ###################
        # checking content
        ###################
        self.assertTemplateUsed(response, "shop_projects/category_detail.html")
        self.assertContains(response, self.category.description)
        self.assertContains(response, self.category.name)
        self.assertContains(response, self.category.pk)

        #######################################
        # checking refs (active functionality)
        #######################################
        # receiving  html of response as str
        response_content: bytes = response.content
        response_content_str: str = response_content.decode()

        # check availability "Update" category
        update_ref = f'/shop_projects/categories/{self.category.pk}/update/'
        count = len(re.findall(f'href="{update_ref}"', response_content_str))
        self.assertEqual(count, 1)

        # check availability "Archive" category
        archive_ref = f'/shop_projects/categories/{self.category.pk}/confirm-delete/'
        count = len(re.findall(f'href="{archive_ref}"', response_content_str))
        self.assertEqual(count, 1)

        # check availability back to all categories (navbar and button)
        archive_ref = f'/shop_projects/categories'
        count = len(re.findall(f'href="{archive_ref}"', response_content_str))
        self.assertEqual(count, 2)


class TestCategoriesListTestCase(TestCase):

    # creation of objects
    @classmethod
    def setUpClass(cls):
        from shop_projects.factories.category import CategoryFactory

        cls.nb_categories = fake.pyint(min_value=2, max_value=7)
        cls.categories = CategoryFactory.create_batch(cls.nb_categories)

    # removal of objects
    @classmethod
    def tearDownClass(cls):
        for category in cls.categories:
            category.delete()

    # checking creation of objects
    def test_get_categories(self):
        # Except "default" category
        qs = Category.objects.filter(~Q(name="default"))
        count = qs.count()
        self.assertEqual(count, self.nb_categories)

    # checking displaying of objects
    def test_get_category_list(self):
        url = reverse("shop_projects:categories")
        response = self.client.get(url)

        ##########################
        # checking right template
        ##########################
        self.assertTemplateUsed(response, "shop_projects/category_list.html")

        categories_qs = (
            Category
            .objects
            .filter(status=Category.Status.AVAILABLE)
            .order_by("id")
            .all()
        )

        ###################
        # checking content
        ###################
        # comparing  test query and response of service
        self.assertQuerySetEqual(
            qs=[project.pk for project in categories_qs],
            values=(p.pk for p in response.context["object_list"]),
        )

        #######################################
        # checking refs (active functionality)
        #######################################
        # receiving  html of response as str
        response_content: bytes = response.content
        response_content_str: str = response_content.decode()
        # response_content_str = response_content_str.replace('"', '&quot;')

        # check availability "create" (navbar and button)
        count = len(re.findall(r'href="/shop_projects/categories/create/"', response_content_str))
        self.assertEqual(count, 2)

        # check availability "back to index" ref (button)
        count = len(re.findall(r'href="/shop_projects/"', response_content_str))
        self.assertEqual(count, 1)

        # assertInHTML work is very bad!!!
        # self.assertInHTML("""href=&quot;/shop_projects/categories/create/&quot;""", response_content_str, count=1)
        # self.assertInHTML('Create new category', response_content_str, count=1)

        # # self.assertContains(response, self.category.name)
        # # self.assertContains(response, self.category.pk)

# href=&quot;/shop_projects/categories/create/&quot;
# href=&quot;/shop_projects/categories/create/&quot;
