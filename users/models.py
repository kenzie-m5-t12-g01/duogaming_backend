import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class CountryChoices(models.TextChoices):
    USA = "United States"
    BRAZIL = "Brazil"


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(
        blank=False,
        unique=True,
        error_messages={
            "unique": ("This email is already being used."),
        },
    )
    country = models.CharField(
        max_length=50,
        choices=CountryChoices.choices,
        default=CountryChoices.BRAZIL,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ("username",)
