from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.views import Response

from utils import mixins
from users.models import User
from users.serializers import UserSerializer
from users.permissions import IsSuperUserOrPostOnly, IsOwnerOrSuperUser

from drf_spectacular.utils import extend_schema


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrPostOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        tags=["Users"], summary="Create user", description="Route to create user"
    )
    def post(self, request, *args, **kwargs) -> Response:
        return self.create(request, *args, **kwargs)

    @extend_schema(
        tags=["Users"], summary="List user", description="Route to list user"
    )
    def get(self, request, *args, **kwargs) -> Response:
        return self.list(request, *args, **kwargs)


class UserDetailView(
    mixins.SoftDeleteMixin,
    generics.RetrieveUpdateDestroyAPIView,
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrSuperUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        tags=["Users"],
        summary="List specific user",
        description="Route to list specific user",
    )
    def get(self, request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=["Users"],
        summary="Update specific user",
        description="Route to partially update user",
    )
    def patch(self, request, *args, **kwargs) -> Response:
        request.data.pop("is_active", None)
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=["Users"], summary="Delete user", description="Route to delete user"
    )
    def delete(self, request, *args, **kwargs) -> Response:
        return self.soft_delete(request, *args, **kwargs)
