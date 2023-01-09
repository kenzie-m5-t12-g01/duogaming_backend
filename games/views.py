from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from games.models import Game
from games.serializers import GameSerializer
from games.permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema


class GameView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_queryset(self):
        route_parameter = self.request.GET.get("genre")

        if route_parameter:
            queryset = Game.objects.filter(genres__name__icontains=route_parameter)
            return queryset

        return super().get_queryset()
    
    @extend_schema(
        tags=["Games"],
        summary= "list games",
        description="Route to list games"
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    @extend_schema(
        tags=["Games"],
        summary= "Create game",
        description="Route to create game"
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class GameDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @extend_schema(
        tags=["Games"],
        summary= "List specific game",
        description="Route to list specific game"
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

    @extend_schema(
        tags=["Games"],
        summary= "Update game",
        description="Route to update specific game"
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    @extend_schema(
        tags=["Games"],
        summary= "Partial update specific game",
        description="Route to Partial update specific game"
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    

    @extend_schema(
        tags=["Games"],
        summary= "Delete game",
        description="Route to delete specific game"
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)