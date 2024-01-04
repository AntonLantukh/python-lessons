from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        abstract = True


class Task(DateMixin):
    class Meta:
        verbose_name_plural = "Tasks"

    title = models.CharField(max_length=256, null=False)
    description = models.CharField(max_length=256, null=True)
    close_date = models.DateTimeField(null=False)
    is_completed = models.BooleanField(default=False, null=False)
    is_deleted = models.BooleanField(default=False, null=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
