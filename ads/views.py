from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from ads.serializers import AdSerializer
from ads.models import Ad
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from week_days.permissions import IsSuperUserOrListOnly


class AdsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        IsSuperUserOrListOnly, 
    ]
    serializer_class = AdSerializer
    queryset = Ad.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

# class AdsDetailView(generics.RetrieveUpdateDestroyAPIView):

#     serializer_class = [AdSerializer]
#     queryset = Ad.objects.all()
