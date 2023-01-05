from rest_framework import serializers
from ads.models import Ad
from week_days.serializers import WeekDaySerializer
from week_days.models import WeekDay

class WeekDaySerializerSerializer(serializers.Serializer):
    day = serializers.CharField()

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

        ad = Ad.objects.create(**validated_data)

        for item in week_days:    
            day_obj = WeekDay.objects.get(**item)
            ad.week_days.add(day_obj)

        ad.save()
        return ad
            