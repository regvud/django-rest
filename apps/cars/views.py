from rest_framework import generics

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarsListCreateView(generics.ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CarRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarModel
    serializer_class = CarSerializer
