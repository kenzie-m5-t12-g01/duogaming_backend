from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Game
from .serializers import GameSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination


class CreateGameView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Game.objects.all()
    serializer_class = GameSerializer


class ListGameView(ListAPIView, PageNumberPagination):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class RetrieveGameView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetailView(UpdateAPIView, DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    
    queryset = Game.objects.all()
    serializer_class = GameSerializer