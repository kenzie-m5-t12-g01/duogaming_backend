# Generated by Django 4.1.5 on 2023-01-09 18:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        error_messages={"unique": "This genre already exists."},
                        max_length=120,
                        unique=True,
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
    ]
