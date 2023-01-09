from rest_framework import serializers
from games.models import Game
from genres.models import Genre


class GenreSerializerSerializer(serializers.Serializer):
    name = serializers.CharField()


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
            "genres",
        ]

    genres = GenreSerializerSerializer(many=True)

    def create(self, validated_data: dict):
        genres = validated_data.pop("genres")
        genres_list = []

        for genre_dict in genres:
            genre_obj, created = Genre.objects.get_or_create(**genre_dict)
            genres_list.append(genre_obj)

        game_obj = Game.objects.create(**validated_data)
        game_obj.genres.set(genres_list)

        return game_obj

    def update(self, instance: Game, validated_data: dict):
        instance.title = validated_data.get("title", instance.title)
        instance.image = validated_data.get("image", instance.image)
        instance.release_date = validated_data.get(
            "release_date", instance.release_date
        )

        instance.save()

        genres = validated_data.pop("genres", None)

        if genres:
            genres_list = []
            for genre_dict in genres:
                genre_obj, created = Genre.objects.get_or_create(**genre_dict)
                genres_list.append(genre_obj)

            instance.genres.set(genres_list)

        return instance
