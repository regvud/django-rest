from django.db import models

from core.models import CoreModel


class CarModel(CoreModel, models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=25)
    year = models.IntegerField()
    seats_count = models.IntegerField()
    body_type = models.CharField(max_length=25)
    engine_volume = models.FloatField()
