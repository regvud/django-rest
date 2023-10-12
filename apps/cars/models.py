from django.db import models

from apps.auto_parks.models import AutoParkModel

from core.models import CoreModel


class CarModel(CoreModel, models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=25)
    year = models.IntegerField()
    seats_count = models.IntegerField()
    body_type = models.CharField(max_length=25)
    engine_volume = models.FloatField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars', null=True)
