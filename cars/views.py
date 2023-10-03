from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from cars.models import CarModel
from cars.serializers import CarSerializer


class CarsListView(APIView):
    @staticmethod
    def get(*args, **kwargs):
        cars = CarSerializer(CarModel.objects.all(), many=True, fields=['id', 'brand', 'year'])

        return Response(cars.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class CarRetrieveDeleteUpdateView(APIView):
    @staticmethod
    def get(*args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()

        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()

        serializer = CarSerializer(car, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()

        serializer = CarSerializer(car, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    @staticmethod
    def delete(*args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()

        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
