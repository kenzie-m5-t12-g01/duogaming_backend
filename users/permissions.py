from rest_framework import permissions

from users.models import User


class IsSuperUserOrPostOnly(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.method not in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.is_superuser


class IsOwnerOrSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: User) -> bool:
        if request.user.is_authenticated:
            if request.user.is_superuser or obj == request.user:
                return True

            return False

        return False
