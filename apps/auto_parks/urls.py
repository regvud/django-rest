from django.urls import path

from .views import AutoParkListCreateView, AutoParkRetrieveUpdateDestroyAPIView, AutoParkCarCreate

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list'),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyAPIView.as_view(), name='auto_park_retrieve_update_destroy'),
    path('/<int:pk>/create', AutoParkCarCreate.as_view(), name='auto_park_create'),
]
