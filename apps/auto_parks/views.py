from rest_framework import generics

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkSerializer, AutoParkShowCarsSerializer


class AutoParkListCreateView(generics.ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AutoParkModel
    serializer_class = AutoParkSerializer


class AutoParkShowCarsView(generics.RetrieveAPIView):
    queryset = AutoParkModel
    serializer_class = AutoParkShowCarsSerializer
