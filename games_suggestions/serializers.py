from rest_framework import serializers

from games_suggestions.models import GameSuggestion


class GameSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSuggestion
        fields = [
            "id",
            "game_title",
            "observations",
            "created_at",
            "user_id",
        ]
        read_only_fields = ["id", "user_id", "created_at"]

    def create(self, validated_data: dict) -> GameSuggestion:
        return GameSuggestion.objects.create(**validated_data)
