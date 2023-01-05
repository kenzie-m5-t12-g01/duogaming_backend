from django.db import models

class WeekDay(models.Model):
    class Meta:
        ordering = ["id",]

    day = models.CharField(max_length=60, unique=True)

