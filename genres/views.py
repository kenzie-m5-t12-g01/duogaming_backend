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
    
    @extend_schema(
        tags=["Genre"],
        summary= "list game genre",
        description="Route to list game genre"
    )
    def get(self, request, *args, **kwargs)->Response:
        return self.list(request, *args, **kwargs)

    @extend_schema(
        tags=["Genre"],
        summary= "Create game genre",
        description="Route to create game genre"
    )
    def post(self, request, *args, **kwargs)->Response:
        return self.create(request, *args, **kwargs)


class GenreDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    @extend_schema(
        tags=["Genre"],
        summary= "list specific game genre",
        description="Route to list specific game genre"
    )
    def get(self, request, *args, **kwargs)->Response:
        return self.retrieve(request, *args, **kwargs)
    
    
    @extend_schema(
        tags=["Genre"],
        summary= "Update game genre",
        description="Route to update specific game genre"
    )
    def patch(self, request, *args, **kwargs)->Response:
        return self.partial_update(request, *args, **kwargs)
    

    @extend_schema(
        tags=["Genre"],
        summary= "Delete game genre",
        description="Route to delete game genre"
    )
    def delete(self, request, *args, **kwargs)->Response:
        return self.destroy(request, *args, **kwargs)
