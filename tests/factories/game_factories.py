from django.contrib.auth.models import AbstractUser
from .user_factories import create_user_with_token
from games.models import Game
from genres.models import Genre
import ipdb

def create_game(game_data = None):


    if not game_data:
        game_data = {
            "title":"league of legends",
            "image":"http://imagem.com.br",
            "release_date": "2009-11-11",
            "genres":[{
		    "name":"moba"
	        }],
        }

    genres = game_data.pop("genres", None)
    game_obj = Game.objects.create(**game_data) 
    genres_list = []

    if genres:
        for genre in genres:
            genre_obj, _ = Genre.objects.get_or_create(**genre)
            game_obj.genres.add(genre_obj)
        
        """ ipdb.set_trace() """
        """ game_obj.genres.set(genres_list) """

    for key, value in game_data.items():
        setattr(game_obj, key, value)

    game_obj.save()

    return game_obj