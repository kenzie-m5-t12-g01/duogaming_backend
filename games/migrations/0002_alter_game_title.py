# Generated by Django 4.1.5 on 2023-01-05 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="title",
            field=models.CharField(max_length=240, unique=True),
        ),
    ]
