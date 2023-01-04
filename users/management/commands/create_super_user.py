from users.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create admin user"

    def add_arguments(self, parser):
        parser.add_argument(
            "--username",
            type=str,
            help="Indicates the admin username to be created",
            default="admin",
        )

        parser.add_argument(
            "--password",
            type=str,
            help="Indicates the admin password to be created",
            default="admin1234",
        )

        parser.add_argument(
            "--email",
            type=str,
            help="Indicates the admin email to be created",
        )

    def handle(self, *args, **kwargs):
        username = kwargs["username"]
        password = kwargs["password"]
        email = kwargs["email"] or f"{username}@example.com"

        username_already_taken = self.is_already_take({"username": username})
        email_already_taken = self.is_already_take({"email": email})

        if username_already_taken:
            raise CommandError(f"Username `{username}` already taken.")

        elif email_already_taken:
            raise CommandError(f"Email `{email}` already taken.")

        User.objects.create_superuser(
            username=username,
            password=password,
            email=email,
        )

        self.stdout.write(
            self.style.SUCCESS(f"Admin `{username}` successfully created!")
        )

    def is_already_take(self, att: dict):
        try:
            return User.objects.get(**att)
        except User.DoesNotExist:
            return False
