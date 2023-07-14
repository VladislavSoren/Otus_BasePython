from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse


class ShopIndexViewTestCase(TestCase):

    def test_index_view_status_ok(self):
        url = reverse("shop_projects:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class GetTaskInfoTestCase(TestCase):
    def test_get_task_info_pending(self):  # pending because even we will not process it
        task_id = "123"
        url = reverse("shop_projects:get-order-task-id", kwargs={"task_id": task_id})
        response = self.client.get(url)
        print(response)

# get-order-task-id