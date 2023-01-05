from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            "id",
            "title",
            "image",
            "release_date",
            "created_at",
            "updated_at",
            # "genres"
        ]