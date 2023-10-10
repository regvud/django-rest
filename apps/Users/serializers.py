from rest_framework import serializers

from apps.auto_parks.serializers import AutoParkHideCarsSerializer
from apps.Users.models import UsersModel


class UsersSerializer(serializers.ModelSerializer):
    auto_parks = AutoParkHideCarsSerializer(read_only=True, many=True)

    class Meta:
        model = UsersModel
        fields = ('id', 'name', 'auto_parks')
