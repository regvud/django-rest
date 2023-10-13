from django_filters import rest_framework as filters

from apps.cars.models import BodyChoices


class CarFilter(filters.FilterSet):
    year_lt = filters.NumberFilter('year', 'lt')
    year_lte = filters.NumberFilter('year', 'lte')
    year_gt = filters.NumberFilter('year', 'gt')
    year_gte = filters.NumberFilter('year', 'gte')
    year = filters.RangeFilter('year')
    brand = filters.CharFilter('brand', 'contains')
    brand_starts = filters.CharFilter('brand', 'startswith')
    brand_ends = filters.CharFilter('brand', 'endswith')
    body = filters.ChoiceFilter('body', choices=BodyChoices.choices)
    order = filters.OrderingFilter(
        fields=[
            'id',
            'brand',
            'year',
            'price'
        ]
    )
