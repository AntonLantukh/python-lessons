from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from tasks.models import Task
from tasks.tests.fixtures import MOCK_USER, MOCK_TASK_DTO


class TasksUpdateViewDBLogicTestCase(TestCase):
    def test_update_task(self):
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

        self.client.post(
            reverse("tasks:update", kwargs={"pk": str(task.id)}) + "?action=complete"
        )  # type: ignore

        updated_task = Task.objects.get(title=MOCK_TASK_DTO["title"])

        self.assertEqual(updated_task.is_completed, True)


class TaskUpdateViewContentTestCase(TestCase):
    def test_page_filled_content(self):
        # Create unfinished task and check the content
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
        self.assertIn("Unfinished".encode(), content)
        self.assertNotIn("Finished".encode(), content)

        # Finish the task and grab the content again
        self.client.post(
            reverse("tasks:update", kwargs={"pk": str(task.id)}) + "?action=complete"
        )  # type: ignore

        response = self.client.get(
            reverse("tasks:detail", kwargs={"pk": str(task.id)})
        )  # type: ignore

        content: bytes = response.content

        self.assertIn(f'{MOCK_TASK_DTO["title"]}'.encode(), content)
        self.assertIn("Finished".encode(), content)
        self.assertNotIn("Unfinished".encode(), content)
