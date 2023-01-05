from django.db import models
import uuid


class Genre (models.Model):
    class Meta:
        ordering = ("name")

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=120, unique=True, error_messages={
        "unique": ("This genre already exists."),
    },)
