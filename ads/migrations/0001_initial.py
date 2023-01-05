# Generated by Django 4.1.5 on 2023-01-04 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("week_days", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ad",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("nickname", models.CharField(max_length=240)),
                ("years_playing", models.IntegerField()),
                ("discord_user", models.CharField(max_length=240)),
                (
                    "day_period",
                    models.CharField(
                        choices=[
                            ("morning", "Morning"),
                            ("afternoon", "Afternoon"),
                            ("night", "Night"),
                            ("not informed", "Default"),
                        ],
                        default="not informed",
                        max_length=30,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ads",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "week_days",
                    models.ManyToManyField(related_name="ads", to="week_days.weekday"),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]
