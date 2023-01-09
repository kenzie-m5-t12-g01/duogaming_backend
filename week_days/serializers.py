from rest_framework import serializers
from week_days.models import WeekDay


class WeekDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekDay
        fields = ["id", "day"]
        read_only_fields = ["id"]

    def create(self, validated_data: dict) -> WeekDay:
        return WeekDay.objects.create(**validated_data)
