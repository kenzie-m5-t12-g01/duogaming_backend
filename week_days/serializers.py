from rest_framework import serializers
from week_days.models import WeekDay

class WeekDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekDay
        fields = ["id", "day", "ads",]
        read_only_fields = ["id", "ads",]


    def create(self, validated_data: dict) -> WeekDay:
        return WeekDay.objects.create(**validated_data)