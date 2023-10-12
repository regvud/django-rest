from django.urls import path

from .views import CarsListCreateView

urlpatterns = [
    path('', CarsListCreateView.as_view(), name='car_list_create'),
]
