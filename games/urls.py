from django.urls import path
from . import views


urlpatterns = [
    path("games/", views.GameView.as_view()),
    path("games/<uuid:pk>/", views.GameDetailView.as_view())
]