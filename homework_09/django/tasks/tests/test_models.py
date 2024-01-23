from django.test import TestCase
from django.contrib.auth.models import User

from tasks.models import Task
from tasks.tests.fixtures import MOCK_USER, MOCK_TASK_DTO


class TaskTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username=MOCK_USER["username"], password=MOCK_USER["password"]
        )
        Task.objects.create(
            title=MOCK_TASK_DTO["title"],
            description=MOCK_TASK_DTO["description"],
            close_date=MOCK_TASK_DTO["close_date"],
            user=user,
        )

    def test_model_create(self):
        task = Task.objects.get(title=MOCK_TASK_DTO["title"])

        self.assertEqual(task.user.username, MOCK_USER["username"])
        self.assertEqual(task.title, MOCK_TASK_DTO["title"])
        self.assertEqual(task.description, MOCK_TASK_DTO["description"])

    def test_model_stringify(self):
        task = Task.objects.get(title=MOCK_TASK_DTO["title"])

        self.assertEqual(
            str(task), f"{MOCK_TASK_DTO['title']} ({MOCK_TASK_DTO['description']})"
        )
