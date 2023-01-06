from rest_framework import permissions
from rest_framework.views import Request, View
from ads.models import Ad
from games.models import Game
from users.models import User
import ipdb

class IsOwnerOrSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Ad) -> bool:
        if request.user.is_authenticated:
            if request.user.is_superuser or obj.user == request.user:
                return True

            return False

        return False

# class OnlyOneAdPerGame(permissions.BasePermission):
#     message = "teste"

#     def has_object_permission(self, request: Request, view: View, obj: Ad) -> bool:
#         user_id = request.user.id
#         game_id = view.kwargs.get("pk")

#         user_obj = User.objects.get(id=user_id)


#         for item in user_obj.ads:

#             print("=" * 100)
#             print(item)
#             print("=" * 100)
#         #     ad_obj = Ad.objects.get(id=item)
#         #     if ad_obj["game_id"] == game_id:
#         #         return False
        
#         # return True
        
