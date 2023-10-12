from rest_framework import serializers

from apps.auto_parks.models import AutoParkModel
from apps.cars.serializers import CarSerializer


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(read_only=True, many=True)

    class Meta:
        model = AutoParkModel
        fields = ('label', 'cars', 'created_at', 'updated_at')
