from http import HTTPStatus

from django.template.response import TemplateResponse
from django.test import TestCase
from django.urls import reverse


class ShopIndexViewTestCase(TestCase):

    def test_index_view_status_ok(self):
        url = reverse("shop_projects:index")
        response: TemplateResponse = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "shop_projects/index.html")
        response_content: bytes = response.content
        response_content_str: str = response_content.decode()
        self.assertInHTML("Shop Index", response_content_str, count=1)
