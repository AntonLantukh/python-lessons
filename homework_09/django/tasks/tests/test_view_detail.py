from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from tasks.models import Task
from tasks.tests.fixtures import MOCK_USER, MOCK_TASK_DTO


class TaskDetailsViewResponseCodeTestCase(TestCase):
    def test_status_code_redirect_guest(self):
        response = self.client.get(reverse("tasks:detail", kwargs={"pk": "1"}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("user:sign_in") + "?next=/tasks/detail/1/", 302
        )

    def test_status_code_not_found(self):
        user = User.objects.create_user(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )
        task = Task.objects.create(
            title=MOCK_TASK_DTO["title"],
            description=MOCK_TASK_DTO["description"],
            close_date=MOCK_TASK_DTO["close_date"],
            user=user,
            is_completed=False,
        )

        self.client.login(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )

        response = self.client.get(reverse("tasks:detail", kwargs={"pk": "1234567"}))

        self.assertEqual(response.status_code, 404)

    def test_status_authenticated_user(self):
        user = User.objects.create_user(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )
        task = Task.objects.create(
            title=MOCK_TASK_DTO["title"],
            description=MOCK_TASK_DTO["description"],
            close_date=MOCK_TASK_DTO["close_date"],
            user=user,
            is_completed=False,
        )

        self.client.login(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )

        response = self.client.get(
            reverse("tasks:detail", kwargs={"pk": str(task.id)})
        )  # type: ignore

        self.assertEqual(response.status_code, 200)


class TasksDetailsViewContextTestCase(TestCase):
    def test_page_filled_context(self):
        user = User.objects.create_user(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )

        task = Task.objects.create(
            title=MOCK_TASK_DTO["title"],
            description=MOCK_TASK_DTO["description"],
            close_date=MOCK_TASK_DTO["close_date"],
            user=user,
            is_completed=False,
        )

        self.client.login(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )

        response = self.client.get(
            reverse("tasks:detail", kwargs={"pk": str(task.id)})
        )  # type: ignore

        task_object = response.context["object"]

        self.assertIsNotNone(task_object)


class TaskDetailsViewContentTestCase(TestCase):
    def test_page_filled_content(self):
        user = User.objects.create_user(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )
        task = Task.objects.create(
            title=MOCK_TASK_DTO["title"],
            description=MOCK_TASK_DTO["description"],
            close_date=MOCK_TASK_DTO["close_date"],
            user=user,
            is_completed=False,
        )
        self.client.login(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )

        response = self.client.get(
            reverse("tasks:detail", kwargs={"pk": str(task.id)})
        )  # type: ignore

        content: bytes = response.content

        self.assertIn(f'{MOCK_TASK_DTO["title"]}'.encode(), content)
        self.assertIn(f'{MOCK_TASK_DTO["description"]}'.encode(), content)
