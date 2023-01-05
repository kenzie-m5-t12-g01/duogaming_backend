from rest_framework import serializers
from ads.models import Ad
from week_days.serializers import WeekDaySerializer
from week_days.models import WeekDay
import ipdb

class AdSerializer(serializers.ModelSerializer):

    week_days = WeekDaySerializer(many=True)
    # game_title = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = [
            "id",
            "nickname",
            # "game_title"
            "years_playing",
            "discord_user",
            "day_period",
            "week_days",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at",]


    # def get_game_title(self, obj: Ad):
    #     return obj.game.game_title

    def create(self, validated_data: dict) -> Ad:
        week_days = validated_data.pop("week_days")
        ipdb.set_trace()

        ad = Ad.objects.create(**validated_data)

        for item in week_days:    
            day_obj = WeekDay.objects.get(**item)
            ad.week_days.add(day_obj)

        ad.save()

        return ad
            