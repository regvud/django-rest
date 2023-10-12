from django.db import models

from core.models import CoreModel


# Create your models here.
class AutoParkModel(CoreModel, models.Model):
    class Meta:
        db_table = 'parks'

    label = models.CharField(max_length=25)
