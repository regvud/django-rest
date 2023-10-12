from django.db import models

from core.models import CoreModel
from apps.users.models import UserModel


# Create your models here.
class AutoParkModel(CoreModel, models.Model):
    class Meta:
        db_table = 'parks'

    label = models.CharField(max_length=25)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks')
