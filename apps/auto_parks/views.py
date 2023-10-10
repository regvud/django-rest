from rest_framework import generics

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkSerializer


class AutoParkListCreateView(generics.ListCreateAPIView):
    queryset = AutoParkModel
    serializer_class = AutoParkSerializer
