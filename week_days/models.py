from django.db import models

class WeekDayChoices(models.TextChoices):
    MON = "mon"
    TUE = "tue"
    WED = "wed" 
    THU = "thu"
    FRI = "fri" 
    SAT = "sat"
    SUN = "sun"

class WeekDay(models.Model):
    class Meta:
        ordering = ["id",]

    day = models.CharField(
        max_length=60, 
        choices=WeekDayChoices.choices,
    )

