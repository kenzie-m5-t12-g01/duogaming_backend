# Generated by Django 4.1.5 on 2023-01-05 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("games_suggestions", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="gamesuggestion",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="games_suggestions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]