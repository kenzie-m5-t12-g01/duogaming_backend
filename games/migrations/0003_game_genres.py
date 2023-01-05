# Generated by Django 4.1.5 on 2023-01-05 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("genres", "0001_initial"),
        ("games", "0002_alter_game_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="genres",
            field=models.ManyToManyField(related_name="genres", to="genres.genre"),
        ),
    ]
