from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken

User: AbstractUser = get_user_model()

def create_user_with_token(user_data=None) -> tuple[AbstractUser, RefreshToken]:
    if not user_data:
        user_data = {
            "username": "matheuszinho",
            "email": "matheus@kenzie.com.br",
            "password": "123456789",
        }

    user = User.objects.create_superuser(**user_data)
    user_token = RefreshToken.for_user(user)

    return user, user_token

def create_non_user_with_token() -> tuple[AbstractUser, RefreshToken]:
    non_user_data = {
        "username": "bielzinho",
        "email": "gabriel@kenzie.com.br",
        "password": "123456789",
    }
    non_user = User.objects.create_user(**non_user_data)
    non_user_token = RefreshToken.for_user(non_user)

    return non_user, non_user_token