from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics

from games_suggestions.models import GameSuggestion
from games_suggestions.serializers import GameSuggestionSerializer
from users.permissions import IsSuperUserOrPostOnly


class GameSuggestionView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUserOrPostOnly]

    queryset = GameSuggestion.objects.all()
    serializer_class = GameSuggestionSerializer
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class GameSuggestionDetailView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = GameSuggestion.objects.all()
    serializer_class = GameSuggestionSerializer
