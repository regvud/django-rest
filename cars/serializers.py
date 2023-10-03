from rest_framework import serializers

from cars.models import CarModel


class DynamicFieldsCategorySerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class CarSerializer(DynamicFieldsCategorySerializer, serializers.Serializer):
    class Meta:
        model = CarModel
        fields = ['id', 'brand', 'year', 'seats_count', 'body_type', 'engine_volume']

    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=25)
    year = serializers.IntegerField()
    seats_count = serializers.IntegerField()
    body_type = serializers.CharField(max_length=25)
    engine_volume = serializers.FloatField()

    def create(self, validated_data):
        return CarModel.objects.create(**validated_data)

    def update(self, instance, validated_data: dict):
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()
        return instance
