from rest_framework import generics
from rest_framework.response import Response

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


# Create your views here.
class CarsListView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()


class CarsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel
