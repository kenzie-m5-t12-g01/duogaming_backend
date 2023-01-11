# Generated by Django 4.1.5 on 2023-01-10 19:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("games", "0001_initial"),
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
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ads",
                        to="games.game",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]
