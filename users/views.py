from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer
from users.permissions import IsSuperUserOrPostOnly, IsOwnerOrSuperUser


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrPostOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrSuperUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def patch(self, request, *args, **kwargs):
        if request.data["is_active"]:
            request.data.pop("is_active")

        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.soft_delete(request, *args, **kwargs)
