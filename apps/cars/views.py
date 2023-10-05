from rest_framework import generics

from apps.cars.filters import car_filter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarsListCreateView(generics.ListCreateAPIView):
    # queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params)


class CarRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarModel
    serializer_class = CarSerializer
