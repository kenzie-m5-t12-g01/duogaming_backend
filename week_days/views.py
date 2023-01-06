from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from week_days.serializers import WeekDaySerializer
from week_days.models import WeekDay    
from rest_framework.permissions import IsAuthenticated
from week_days.pagination import WeekDayPagination

class WeekDayListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = WeekDaySerializer
    queryset = WeekDay.objects.all()
    pagination_class = WeekDayPagination
