from django.db import models


# Create your models here.

# - марка машини
# - рік випуску
# - кількість місць
# - тип кузову
# - об'єм двигуна (float)
# less11
class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=25)
    year = models.IntegerField()
    seats_count = models.IntegerField()
    body_type = models.CharField(max_length=25)
    engine_volume = models.FloatField()

