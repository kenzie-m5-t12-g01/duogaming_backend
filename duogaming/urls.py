from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("users.urls")),
    path("api/", include("ads.urls")),
    path("api/", include("week_days.urls")),
    path("api/", include("games.urls")),
    path("api/", include("games_suggestions.urls")),
    path("api/", include("genres.urls")),
]
