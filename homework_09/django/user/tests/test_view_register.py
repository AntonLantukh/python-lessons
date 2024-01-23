from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from user.tests.fixtures import REGISTER_USER_CLIENT


class UserRegisterViewTestCase(TestCase):
    def test_page_register(self):
        #  Checking user is not logged in and registered
        hasUser = User.objects.filter(
            username=REGISTER_USER_CLIENT["username"]
        ).exists()
        self.assertEqual(hasUser, False)

        response = self.client.get(path=reverse("tasks:list"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("user:sign_in") + "?next=/tasks/", 302)

        # Register and check again
        self.client.post(path=reverse("user:sign_up"), data=REGISTER_USER_CLIENT)

        hasUser = User.objects.filter(
            username=REGISTER_USER_CLIENT["username"]
        ).exists()

        self.assertEqual(hasUser, True)

        response = self.client.get(path=reverse("tasks:list"))

        self.assertEqual(response.status_code, 200)
