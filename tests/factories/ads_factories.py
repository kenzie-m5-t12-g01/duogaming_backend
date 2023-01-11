from django.contrib.auth.models import AbstractUser
from .user_factories import create_user_with_token
from ads.models import Ad

def create_ads_with_su(ads_data: dict = None, user: AbstractUser = None) -> Ad:
    if not user:
        user, _ = create_user_with_token()
    
    if not ads_data:
        ads_data = {
            "nickname":"matheuzin",
            "game_title": "league of legends",
            "years_playing": 5,
            "discord_user": "matheuszinSp",
            "day_period": "night",
            "week_days": [
		        {"day":"mon"}
	        ]
        }
    
    ads = Ad.objects.create(**ads_data, user=user)

    return ads