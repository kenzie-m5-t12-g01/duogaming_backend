import uuid
from django.db import models

class GameSuggestion(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    game_title = models.CharField(max_length=120)
    observations = models.TextField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="games_suggestions",
    )

    class Meta:
        ordering = "created_at",
