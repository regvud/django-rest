from django.core import validators as v
from django.db import models

from apps.users.models import UserModel

from core.enum.regex_enum import RegEx
from core.models import CoreModel


# Create your models here.
class AutoParkModel(CoreModel):
    class Meta:
        db_table = 'parks'

    label = models.CharField(max_length=20, validators=[v.RegexValidator(RegEx.LABEL.pattern, RegEx.LABEL.msg)])
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks')
