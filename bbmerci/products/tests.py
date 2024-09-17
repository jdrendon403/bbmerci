from django.test import TestCase
from django.urls import reverse

class ProductListTest(TestCase):

    def test_should_return_200(self):
        url = reverse("list_product")
        response = self.client.get(url)
        # breakpoint()
        self.assertEqual(response.status_code, 200)
