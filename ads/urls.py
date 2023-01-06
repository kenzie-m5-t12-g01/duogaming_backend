from django.urls import path
from ads import views

urlpatterns = [
    path("games/<uuid:pk>/ads/", views.AdsView.as_view()),
    path("ads/", views.AdsListView.as_view()),
    path("ads/<uuid:pk>/", views.AdsDetailView.as_view())
]