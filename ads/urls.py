from django.urls import path
from ads import views

urlpatterns = [
    path("game/<uuid:pk>/ads/", views.AdsView.as_view()),
    # path("ads/<int:id>", views.AdsDetailView.as_view())
]