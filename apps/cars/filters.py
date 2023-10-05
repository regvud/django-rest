from django.db.models import QuerySet
from django.http import QueryDict

from apps.cars.models import CarModel


def car_filter(cars: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()

    for k, v in cars.items():
        match k:
            case 'year_lt':
                qs = qs.filter(year__lt=v)

    return qs
