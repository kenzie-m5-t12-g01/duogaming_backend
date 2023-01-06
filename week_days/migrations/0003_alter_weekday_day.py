# Generated by Django 4.1.5 on 2023-01-05 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("week_days", "0002_alter_weekday_day"),
    ]

    operations = [
        migrations.AlterField(
            model_name="weekday",
            name="day",
            field=models.CharField(
                choices=[
                    ("mon", "Mon"),
                    ("tue", "Tue"),
                    ("wed", "Wed"),
                    ("thu", "Thu"),
                    ("fri", "Fri"),
                    ("sat", "Sat"),
                    ("sun", "Sun"),
                ],
                max_length=60,
            ),
        ),
    ]
