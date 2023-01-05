from django.urls import path
from . import views


urlpatterns = [
    path("games/new", views.CreateGameView.as_view()),
    path("games/", views.ListGameView.as_view()),
    path("games/<uuid:pk>/retrieve/", views.RetrieveGameView.as_view()),
    path("games/<uuid:pk>/", views.GameDetailView.as_view())
]