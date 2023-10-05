from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.serializers import ValidationError

from apps.cars.models import CarModel


def car_filter(cars: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()

    for k, v in cars.items():
        match k:
            # brand
            case 'brand':
                qs = qs.filter(brand=v)
            case 'brand_contains':
                qs = qs.filter(brand__contains=v)
            case 'brand_ends':
                qs = qs.filter(brand__endswith=v)
            case 'brand_starts':
                qs = qs.filter(brand__startswith=v)

            case 'asc_brand':
                qs = qs.order_by('brand')
            case 'desc_brand':
                qs = qs.order_by('-brand')

            # year
            case 'year':
                qs = qs.filter(year=v)
            case 'year_gt':
                qs = qs.filter(year__gt=v)
            case 'year_gte':
                qs = qs.filter(year__gte=v)
            case 'year_lt':
                qs = qs.filter(year__lt=v)
            case 'year_lte':
                qs = qs.filter(year__lte=v)

            case 'asc_year':
                qs = qs.order_by('year')
            case 'desc_year':
                qs = qs.order_by('-year')

            # seats
            case 'seats_count':
                qs = qs.filter(seats_count=v)
            case 'seats_count_gt':
                qs = qs.filter(seats_count__gt=v)
            case 'seats_count_gte':
                qs = qs.filter(seats_count__gte=v)
            case 'seats_count_lt':
                qs = qs.filter(seats_count__lt=v)
            case 'seats_count_lte':
                qs = qs.filter(seats_count__lte=v)

            case 'asc_seats_count':
                qs = qs.order_by('seats_count')
            case 'desc_seats_count':
                qs = qs.order_by('-seats_count')

            # body_type
            case 'body_type':
                qs = qs.filter(body_type=v)
            case 'body_type_contains':
                qs = qs.filter(body_type__contains=v)
            case 'body_type_ends':
                qs = qs.filter(body_type__endswith=v)
            case 'body_type_starts':
                qs = qs.filter(body_type__startswith=v)

            case 'asc_body_type':
                qs = qs.order_by('body_type')
            case 'desc_body_type':
                qs = qs.order_by('-body_type')

            # engine_volume
            case 'engine_volume':
                qs = qs.filter(engine_volume=v)

            case 'asc_engine_volume':
                qs = qs.order_by('engine_volume')
            case 'desc_engine_volume':
                qs = qs.order_by('-engine_volume')

            # default
            case _:
                raise ValidationError({'details': f'{k} is not allowed here'})

    return qs
