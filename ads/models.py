from django.db import models
import uuid

class DayPeriodChoice(models.TextChoices):
    MORNING = "morning"
    AFTERNOON = "afternoon"
    NIGHT = "night"
    DEFAULT = "not informed"

class Ad(models.Model):
    class Meta:
        ordering = ["id",]
    
    id = models.UUIDField(
        default=uuid.uuid4, 
        primary_key=True, 
        editable=True,
    )
    nickname = models.CharField(max_length=240, unique=True)
    years_playing = models.IntegerField()
    discord_user = models.CharField(max_length=240)
    day_period = models.CharField(
        max_length=30,
        choices=DayPeriodChoice.choices,
        default=DayPeriodChoice.DEFAULT,
    )
    
    week_days = models.ManyToManyField(
        "week_days.WeekDay", 
        related_name="ads",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="ads",
    )
    game = models.ForeignKey(
        "games.Game",
        on_delete=models.CASCADE,
        related_name="ads"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)