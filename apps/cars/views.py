from rest_framework import generics

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


# Create your views here.
class CarsListCreateView(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()


class CarsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel
