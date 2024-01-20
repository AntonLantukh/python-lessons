from django.contrib import admin

# Register your models here.
from .models import Task


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "close_date", "user", "is_completed", "is_deleted"]
    list_display_links = ["id", "title"]
