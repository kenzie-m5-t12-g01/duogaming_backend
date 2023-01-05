from django.urls import path

from games_suggestions.views import GameSuggestionView, GameSuggestionDetailView


urlpatterns = [
    path("games-suggestions/", GameSuggestionView.as_view()),
    path("games-suggestions/<uuid:pk>/", GameSuggestionDetailView.as_view()),
]
