from django.urls import path
from rest_framework_simplejwt import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from users.views import UserView, UserDetailView


urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<uuid:pk>/", UserDetailView.as_view()),
    path("users/login/", views.TokenObtainPairView.as_view()),
    # schema download
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # doc
    path("doc/", SpectacularSwaggerView.as_view(url_name='schema'), name="swagger-ui")
]
