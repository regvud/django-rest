from rest_framework import serializers
from .models import UserModel
from ..auto_parks.serializers import AutoParkSerializer


class UserSerializer(serializers.ModelSerializer):
    auto_parks = AutoParkSerializer(read_only=True, many=True)

    class Meta:
        model = UserModel
        fields = ('name', 'age', 'auto_parks')
