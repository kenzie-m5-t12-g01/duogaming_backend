from rest_framework import generics, serializers
from rest_framework.views import Response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import get_object_or_404

from games.models import Game
from users.models import User

from ads.models import Ad
from ads.serializers import AdSerializer
from ads.permissions import IsOwnerOrSuperUser


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

        game_obj = get_object_or_404(Game, id=game_id)
        ad_already_exists = Ad.objects.filter(game_id=game_id, user_id=user_id)

        if ad_already_exists:
            raise serializers.ValidationError("You already have an ad for this game.")

        else:
            return serializer.save(
                user=self.request.user,
                game=game_obj,
            )


class AdsUserView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AdSerializer

    def get_queryset(self):
        user_id = self.kwargs["pk"]
        get_object_or_404(User, id=user_id)

        queryset = Ad.objects.filter(user_id=user_id)

        return queryset


class AdsListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class AdsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrSuperUser]
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
