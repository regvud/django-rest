from django.urls import path

from .views import CarsRetrieveUpdateDestroyAPIView, CarsListView

urlpatterns = [
    path('', CarsListView.as_view(), name='car_list_create'),
    path('/<int:pk>', CarsRetrieveUpdateDestroyAPIView.as_view(), name='car_retrieve_update_destroy'),

]
