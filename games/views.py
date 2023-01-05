from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from games.models import Game
from games.serializers import GameSerializer
from games.permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination


class GameView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
    queryset = Game.objects.all()
    serializer_class = GameSerializer