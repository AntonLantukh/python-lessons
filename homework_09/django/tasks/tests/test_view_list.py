from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from tasks.models import Task
from tasks.tests.fixtures import MOCK_USER, MOCK_TASK_DTO


class TasksListViewResponseCodeTestCase(TestCase):
    def test_status_code_redirect_guest(self):
        response = self.client.get(reverse("tasks:list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("user:sign_in") + "?next=/tasks/", 302)

    def test_status_authenticated_user(self):
        User.objects.create_user(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )
        self.client.login(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )

        response = self.client.get(reverse("tasks:list"))

        self.assertEqual(response.status_code, 200)


class TasksListViewContextTestCase(TestCase):
    def test_page_empty_context(self):
        User.objects.create_user(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )
        self.client.login(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )

        response = self.client.get(reverse("tasks:list"))

        finished_tasks = response.context["finished_tasks"]
        unfinished_tasks = response.context["unfinished_tasks"]

        self.assertEqual(len(finished_tasks), 0)
        self.assertEqual(len(unfinished_tasks), 0)

    def test_page_filled_context(self):
        user = User.objects.create_user(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )

        Task.objects.create(
            title=MOCK_TASK_DTO["title"],
            description=MOCK_TASK_DTO["description"],
            close_date=MOCK_TASK_DTO["close_date"],
            user=user,
            is_completed=False,
        )

        Task.objects.create(
            title=MOCK_TASK_DTO["title"],
            description=MOCK_TASK_DTO["description"],
            close_date=MOCK_TASK_DTO["close_date"],
            user=user,
            is_completed=True,
        )

        self.client.login(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )

        response = self.client.get(reverse("tasks:list"))

        finished_tasks = response.context["finished_tasks"]
        unfinished_tasks = response.context["unfinished_tasks"]

        self.assertEqual(len(finished_tasks), 1)
        self.assertEqual(len(unfinished_tasks), 1)


class TasksListViewContentTestCase(TestCase):
    def test_page_empty_content(self):
        User.objects.create_user(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )
        self.client.login(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )

        response = self.client.get(reverse("tasks:list"))

        content: bytes = response.content

        self.assertIn(b"No unfinished tasks yet", content)
        self.assertIn(b"No finished tasks yet", content)

    def test_page_filled_content(self):
        user = User.objects.create_user(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )
        Task.objects.create(
            title=MOCK_TASK_DTO["title"],
            description=MOCK_TASK_DTO["description"],
            close_date=MOCK_TASK_DTO["close_date"],
            user=user,
            is_completed=False,
        )
        self.client.login(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )

        response = self.client.get(reverse("tasks:list"))

        content: bytes = response.content

        self.assertIn(f'{MOCK_TASK_DTO["title"]}'.encode(), content)
        self.assertIn(f'{MOCK_TASK_DTO["description"]}'.encode(), content)
        self.assertIn(b"No finished tasks yet", content)
        self.assertNotIn(b"No unfinished tasks yet", content)
