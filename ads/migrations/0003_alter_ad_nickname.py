# Generated by Django 4.1.5 on 2023-01-06 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="nickname",
            field=models.CharField(max_length=240),
        ),
    ]