from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from week_days.models import WeekDay
from week_days.pagination import WeekDayPagination
from week_days.serializers import WeekDaySerializer

from drf_spectacular.utils import extend_schema


class WeekDayListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = WeekDaySerializer
    queryset = WeekDay.objects.all()
    pagination_class = WeekDayPagination

    @extend_schema(
        tags=["WeekDay"],
        summary="list week day",
        description="Route to list days os the week",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
