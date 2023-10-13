from django.urls import path

from .views import AutoParkCarCreate, AutoParkListView, AutoParkRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', AutoParkListView.as_view(), name='auto_park_list'),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyAPIView.as_view(), name='auto_park_retrieve_update_destroy'),
    path('/<int:pk>/create', AutoParkCarCreate.as_view(), name='auto_park_create_car'),
]
