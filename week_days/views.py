from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from week_days.serializers import WeekDaySerializer
from week_days.models import WeekDay    
from week_days.permissions import IsSuperUserOrListOnly
from rest_framework.pagination import PageNumberPagination

class WeekDayPagination(PageNumberPagination):
    page_size = 7

class WeekDayView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrListOnly]
    serializer_class = WeekDaySerializer
    queryset = WeekDay.objects.all()
    pagination_class = WeekDayPagination
    

class WeekDayDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrListOnly]
    serializer_class = WeekDaySerializer
    queryset = WeekDay.objects.all()
    lookup_url_kwarg = "id"
