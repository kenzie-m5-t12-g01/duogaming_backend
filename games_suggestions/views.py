from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics
from rest_framework.views import Response

from games_suggestions.models import GameSuggestion
from games_suggestions.serializers import GameSuggestionSerializer
from users.permissions import IsSuperUserOrPostOnly

from drf_spectacular.utils import extend_schema


class GameSuggestionView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUserOrPostOnly]

    queryset = GameSuggestion.objects.all()
    serializer_class = GameSuggestionSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @extend_schema(
        tags=["GameSuggestion"],
        summary="list game suggestions",
        description="Route to list game suggestions",
    )
    def get(self, request, *args, **kwargs) -> Response:
        return self.list(request, *args, **kwargs)

    @extend_schema(
        tags=["GameSuggestion"],
        summary="Create game suggestion",
        description="Route to create game suggestion",
    )
    def post(self, request, *args, **kwargs) -> Response:
        return self.create(request, *args, **kwargs)


class GameSuggestionDetailView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = GameSuggestion.objects.all()
    serializer_class = GameSuggestionSerializer

    @extend_schema(
        tags=["GameSuggestion"],
        summary="List specific game suggestion",
        description="Route to List specific game suggestion",
    )
    def get(self, request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=["GameSuggestion"],
        summary="Delete game suggestion",
        description="Route to delete game suggestion",
    )
    def delete(self, request, *args, **kwargs) -> Response:
        return self.destroy(request, *args, **kwargs)
