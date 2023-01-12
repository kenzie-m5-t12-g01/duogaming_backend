from rest_framework import status
from rest_framework.response import Response


class SoftDeleteMixin:
    def soft_delete(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data={"is_active": False}, partial=True
        )
        serializer.is_valid(raise_exception=True)

        self.perform_soft_delete(serializer)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_soft_delete(self, serializer):
        serializer.save()
