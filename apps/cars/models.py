import datetime

from django.core import validators as v
from django.db import models

from apps.auto_parks.models import AutoParkModel
from apps.cars.choices import BodyChoices

from core.enum.regex_enum import RegEx
from core.models import CoreModel


class CarModel(CoreModel):
    class Meta:
        db_table = 'cars'
        ordering = ['id']

    brand = models.CharField(max_length=20, validators=[v.RegexValidator(RegEx.BRAND.pattern, RegEx.BRAND.msg)])
    year = models.IntegerField(
        validators=[v.MinValueValidator(1950), v.MaxValueValidator(datetime.datetime.now().year)])
    price = models.IntegerField(validators=[v.MinValueValidator(0), v.MaxValueValidator(1000000)])
    seats = models.IntegerField(validators=[v.MinValueValidator(0), v.MaxValueValidator(20)])
    body = models.CharField(max_length=9, choices=BodyChoices.choices)
    engine_volume = models.FloatField(validators=[v.MinValueValidator(0.8), v.MaxValueValidator(10)])
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
