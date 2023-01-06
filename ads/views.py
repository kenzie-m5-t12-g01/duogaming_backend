from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from ads.serializers import AdSerializer
from ads.models import Ad
from rest_framework.permissions import IsAuthenticated
from ads.permissions import IsOwnerOrSuperUser
from django.shortcuts import get_object_or_404
from games.models import Game



class AdsView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AdSerializer

    def perform_create(self, serializer):
        game_id = self.kwargs["pk"]
        game_obj = get_object_or_404(Game, id=game_id)

        return serializer.save(
            user=self.request.user,
            game=game_obj,
        )

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
        