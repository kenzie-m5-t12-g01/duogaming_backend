from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from ads.serializers import AdSerializer
from ads.models import Ad
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from week_days.permissions import IsSuperUserOrListOnly
from django.shortcuts import get_object_or_404
from games.models import Game


class AdsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AdSerializer
    queryset = Ad.objects.all()

    def perform_create(self, serializer):
        game_id = self.kwargs["pk"]
        game_obj = get_object_or_404(Game, id=game_id)

        return serializer.save(
            user=self.request.user,
            game=game_obj,
        )

class AdsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    

    serializer_class = [AdSerializer]
    queryset = Ad.objects.all()
