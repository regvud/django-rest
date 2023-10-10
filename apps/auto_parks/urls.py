from django.urls import path

from apps.auto_parks.views import AutoParkListCreateView, AutoParkRetrieveUpdateDestroyView, AutoParkShowCarsView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_parks_list_create'),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view(), name='auto_parks_retrieve_update_destroy'),
    path('/<int:pk>/cars', AutoParkShowCarsView.as_view(), name='auto_parks_show_cars')
]
