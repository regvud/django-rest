from django.urls import path

from apps.auto_parks.views import AutoParkListCreateView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list_create'),
]
