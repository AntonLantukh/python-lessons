from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from tasks.models import Task
from tasks.tests.fixtures import MOCK_USER, MOCK_TASK_DTO


class TasksDeleteViewTestCase(TestCase):
    def test_page_delete_content(self):
        # Create a new task and check if it exists
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

        # Task exists
        response = self.client.get(
            reverse("tasks:detail", kwargs={"pk": str(task.id)})
        )  # type: ignore

        self.assertEqual(response.status_code, 200)

        # Deleting it and grabbing the content again
        self.client.post(
            reverse("tasks:delete", kwargs={"pk": str(task.id)})
        )  # type: ignore

        response = self.client.get(
            reverse("tasks:detail", kwargs={"pk": str(task.id)})
        )  # type: ignore

        self.assertEqual(response.status_code, 404)
