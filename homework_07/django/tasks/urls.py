from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.list, name="list"),
    path("create", views.create, name="create"),
    path("comlete/<str:task_id>", views.complete, name="complete"),
    path("uncomlete/<str:task_id>", views.uncomplete, name="uncomplete"),
    path("delete/<str:task_id>", views.delete, name="delete"),
]
