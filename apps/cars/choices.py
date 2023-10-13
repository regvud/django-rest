from django.db import models


class BodyChoices(models.TextChoices):
    sedan = 'sedan',
    suv = 'suv',
    universal = 'universal',
    coupe = 'coupe'
