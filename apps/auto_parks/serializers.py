from rest_framework import serializers

from apps.auto_parks.models import AutoParkModel


class AutoParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'created_at', 'updated_at', 'cars')
