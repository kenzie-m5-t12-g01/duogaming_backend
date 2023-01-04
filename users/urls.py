from django.urls import path
from rest_framework_simplejwt import views

from users.views import UserView, UserDetailView


urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<uuid:pk>/", UserDetailView.as_view()),
    path("users/login/", views.TokenObtainPairView.as_view()),
]
