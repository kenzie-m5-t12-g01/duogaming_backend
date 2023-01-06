from rest_framework import serializers
from ads.models import Ad
from week_days.models import WeekDay, WeekDayChoices

class WeekDaySerializerSerializer(serializers.Serializer):
    day = serializers.ChoiceField(
        choices=WeekDayChoices.choices,
    )

class AdSerializer(serializers.ModelSerializer):
    week_days = WeekDaySerializerSerializer(many=True)

    class Meta:
        model = Ad
        fields = [
            "id",
            "nickname",
            "years_playing",
            "discord_user",
            "day_period",
            "week_days",
            "user_id",
            "game_id",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id", 
            "created_at", 
            "updated_at", 
            "user_id", 
            "game_id",
        ]

    def create(self, validated_data: dict) -> Ad:
        week_days = validated_data.pop("week_days")

        week_days_valid = []
        for item in week_days:    
            day_obj, _ = WeekDay.objects.get_or_create(**item)
            week_days_valid.append(day_obj)

        ad = Ad.objects.create(**validated_data)
        ad.week_days.set(week_days_valid)

        return ad
        
            