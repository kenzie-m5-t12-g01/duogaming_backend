from rest_framework import serializers

from games_suggestions.models import GameSuggestion


class GameSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSuggestion
        fields = "__all__"
        read_only_fields = ["id", "user_id"]

    def create(self, validated_data: dict) -> GameSuggestion:
        return GameSuggestion.objects.create(**validated_data)
