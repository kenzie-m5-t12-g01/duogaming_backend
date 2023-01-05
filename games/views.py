from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from games.models import Game
from games.serializers import GameSerializer
from games.permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination


class GameView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_queryset(self):
        route_parameter = self.request.GET.get("genre")

        if route_parameter:
            queryset = Game.objects.filter(genres__name__icontains=route_parameter)
            return queryset

        return super().get_queryset()


class GameDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
    queryset = Game.objects.all()
    serializer_class = GameSerializer