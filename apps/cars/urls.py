from django.urls import path

from apps.cars.views import CarRetrieveUpdateDestroy, CarsListCreateView

urlpatterns = [
    path('', CarsListCreateView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroy.as_view())
]
