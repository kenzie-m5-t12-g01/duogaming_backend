from rest_framework import permissions
from rest_framework.views import Request, View

from ads.models import Ad
from games.models import Game
from users.models import User


class IsOwnerOrSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Ad) -> bool:
        if request.user.is_authenticated:
            if request.user.is_superuser or obj.user == request.user:
                return True

            return False

        return False
