from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from ads.serializers import AdSerializer
from ads.models import Ad
from rest_framework.permissions import IsAuthenticated
from ads.permissions import IsOwnerOrSuperUser
from django.shortcuts import get_object_or_404
from games.models import Game
from users.models import User

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
        game_obj = get_object_or_404(Game, id=game_id)

        self.check_object_permissions(self.request, game_obj)

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
        