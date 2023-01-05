from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from week_days.serializers import WeekDaySerializer
from week_days.models import WeekDay    
from week_days.permissions import IsSuperUserOrListOnly


class WeekDayView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrListOnly]
    serializer_class = WeekDaySerializer
    queryset = WeekDay.objects.all()
    

class WeekDayDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUserOrListOnly]
    serializer_class = WeekDaySerializer
    queryset = WeekDay.objects.all()
    lookup_url_kwarg = "id"
