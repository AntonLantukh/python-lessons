import datetime
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from tasks.models import Task
from tasks.tests.fixtures import MOCK_TASK_CLIENT, MOCK_USER, MOCK_TASK_DTO


class TasksCreateViewTestCase(TestCase):
    def test_page_create_content(self):
        #  Checking no task exists
        hasTask = Task.objects.filter(title=MOCK_TASK_CLIENT["title"]).exists()
        self.assertEqual(hasTask, False)

        # Creating new task via endpoint
        user = User.objects.create_user(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )

        self.client.login(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )

        self.client.post(path=reverse("tasks:create"), data=MOCK_TASK_CLIENT)

        # Getting task again
        task = Task.objects.get(title=MOCK_TASK_CLIENT["title"])

        self.assertEqual(task.title, MOCK_TASK_DTO["title"])
        self.assertEqual(task.description, MOCK_TASK_DTO["description"])
        self.assertEqual(
            task.close_date,
            datetime.datetime.fromisoformat(MOCK_TASK_DTO["close_date"]),
        )
        self.assertEqual(task.user.id, user.id)  # type: ignore
