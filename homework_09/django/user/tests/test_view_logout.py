from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from user.tests.fixtures import LOGIN_USER_DTO


class UserLogoutViewTestCase(TestCase):
    def test_page_logout(self):
        User.objects.create_user(
            username=LOGIN_USER_DTO["username"], password=LOGIN_USER_DTO["password"]
        )
        self.client.login(
            username=LOGIN_USER_DTO["username"], password=LOGIN_USER_DTO["password"]
        )

        #  Checking user is logged in
        response = self.client.get(path=reverse("tasks:list"))
        self.assertEqual(response.status_code, 200)

        # Log out and check again
        self.client.post(path=reverse("user:sign_out"))

        response = self.client.get(path=reverse("tasks:list"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("user:sign_in") + "?next=/tasks/", 302)
