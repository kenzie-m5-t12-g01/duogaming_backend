from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework import generics

from games_suggestions.models import GameSuggestion
from games_suggestions.serializers import GameSuggestionSerializer
from users.permissions import IsSuperUserOrPostOnly


class GameSuggestionView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrPostOnly]

    queryset = GameSuggestion.objects.all()
    serializer_class = GameSuggestionSerializer


class GameSuggestionDetailView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = GameSuggestion.objects.all()
    serializer_class = GameSuggestionSerializer
