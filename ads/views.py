from rest_framework import generics, serializers
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import get_object_or_404

from games.models import Game
from users.models import User

from ads.models import Ad
from ads.serializers import AdSerializer
from ads.permissions import IsOwnerOrSuperUser

from drf_spectacular.utils import extend_schema


class AdsGameView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AdSerializer
    
    def get_queryset(self):
        game_id = self.kwargs["pk"]
        get_object_or_404(Game, id=game_id)

        queryset = Ad.objects.filter(game_id=game_id)

        return queryset

    def perform_create(self, serializer):
        game_id = self.kwargs["pk"]
        user_id = self.request.user.id
        nickname = self.request.data["nickname"]

        game_obj = get_object_or_404(Game, id=game_id)

        ad_already_exists = Ad.objects.filter(game_id=game_id, user_id=user_id)
        nickname_already_exists = Ad.objects.filter(game_id=game_id, nickname=nickname)

        if ad_already_exists:
            raise serializers.ValidationError("You already have an ad for this game.")

        elif nickname_already_exists:
            raise serializers.ValidationError(
                "There is already an ad with the same nickname for this game."
            )

        return serializer.save(
            user=self.request.user,
            game=game_obj,
        )
    
    @extend_schema(
        tags=["Ads"],
        summary= "list game ads",
        description="Route to list game ads"
    )
    def get(self, request, *args, **kwargs)->Response:
        return self.list(request, *args, **kwargs)

    @extend_schema(
        tags=["Ads"],
        summary= "Create game ads",
        description="Route to create game ads"
    )
    def post(self, request, *args, **kwargs)->Response:
        return self.create(request, *args, **kwargs)


class AdsUserView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AdSerializer

    def get_queryset(self):
        user_id = self.kwargs["pk"]
        get_object_or_404(User, id=user_id)

        queryset = Ad.objects.filter(user_id=user_id)

        return queryset
    
    @extend_schema(
        tags=["Ads"],
        summary= "list user ads",
        description="Route to list user ads"
    )
    def get(self, request, *args, **kwargs)->Response:
        return self.list(request, *args, **kwargs)


  
class AdsListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AdSerializer
    queryset = Ad.objects.all()

    @extend_schema(
        tags=["Ads"],
        summary= "list ads",
        description="Route to list ads"
    )
    def get(self, request, *args, **kwargs)->Response:
        return self.list(request, *args, **kwargs)



class AdsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrSuperUser]
    serializer_class = AdSerializer
    queryset = Ad.objects.all()

    @extend_schema(
        tags=["Ads"],
        summary= "list specific ads",
        description="Route to list specific ads"
    )
    def get(self, request, *args, **kwargs)->Response:
        return self.retrieve(request, *args, **kwargs)


    @extend_schema(
        tags=["Ads"],
        summary= "Update specific ads",
        description="Route to partially update specific ads"
    )
    def patch(self, request, *args, **kwargs)->Response:
        return self.partial_update(request, *args, **kwargs)


    @extend_schema(
        tags=["Ads"],
        summary= "Delete ads",
        description="Route to delete specific ads"
    )
    def delete(self, request, *args, **kwargs)->Response:
        return self.destroy(request, *args, **kwargs)
