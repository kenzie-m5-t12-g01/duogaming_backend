from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework.views import  Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from genres.permissions import IsAdminOrReadOnly
from drf_spectacular.utils import extend_schema


class GenreView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get(self, request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs) -> Response:
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs) -> Response:
        return self.destroy(request, *args, **kwargs)
