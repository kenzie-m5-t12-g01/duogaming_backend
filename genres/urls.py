from genres.views import GenreView, GenreDetailView
from django.urls import path


urlpatterns = {
    path("genres/", GenreView.as_view()),
    path("genres/<uuid:pk>/", GenreDetailView.as_view())
}
