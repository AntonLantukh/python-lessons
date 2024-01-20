from django.urls import path

from .views import TasksListView, TasksDetailView, TasksCreateView, TasksDeleteView, TasksUpdateView

app_name = "tasks"

urlpatterns = [
    path("", TasksListView.as_view(), name="list"),
    path("create", TasksCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", TasksDetailView.as_view(), name="detail"),
    path("delete/<int:pk>", TasksDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", TasksUpdateView.as_view(), name="update"),
]
