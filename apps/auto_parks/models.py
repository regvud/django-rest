from django.db import models

from apps.Users.models import UsersModel

from core.models import CoreModel


# Create your models here.
class AutoParkModel(CoreModel, models.Model):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=20)
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE, related_name='auto_parks', null=True)
