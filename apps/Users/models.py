from django.db import models

from core.models import CoreModel


class UsersModel(CoreModel, models.Model):
    class Meta:
        db_table = 'users'

    name = models.CharField(max_length=20)
