# Generated by Django 5.0 on 2024-01-03 19:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0006_alter_task_is_deleted"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="is_complete",
            new_name="is_completed",
        ),
    ]
