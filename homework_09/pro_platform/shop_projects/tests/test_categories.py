from django.db.models import Q
from django.test import TestCase
from django.urls import reverse

from shop_projects.models import Category


class TestCategoriesListTestCase(TestCase):

    # creation of object
    @classmethod
    def setUpClass(cls):
        # scope on other methods
        cls.category = Category.objects.create(
            name="un_cat_name",
            description='desk1'
        )

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
        self.assertTemplateUsed(response, "shop_projects/category_detail.html")
        self.assertContains(response, self.category.description)
        self.assertContains(response, self.category.name)
        self.assertContains(response, self.category.pk)
