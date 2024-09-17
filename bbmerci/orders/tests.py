from django.test import TestCase
from django.urls import reverse

class MyOrderViewTest(TestCase):

    def test_no_logged_redirected_to_login(self):
        url = reverse("my_order")
        response = self.client.get(url)
        # breakpoint()
        self.assertEqual(response.url, '/users/login?next=/orders/my_order')