from django.db import models

from apps.auto_parks.models import AutoParkModel
from core.models import CoreModel


class CarModel(CoreModel, models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    price = models.IntegerField()
    seats = models.IntegerField()
    body = models.CharField(max_length=9)
    engine_volume = models.FloatField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
