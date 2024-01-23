from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = "admin"
            password = "12345"
            email = "admin@admin.com"
            print("Creating account for %s (%s)" % (username, email))
            admin = User.objects.create_superuser(
                username=username, password=password, email=email
            )
            admin.is_active = True
            admin.save()
        else:
            print("Admin account can only be initialized if no account exists")
