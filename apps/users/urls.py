from django.urls import path

from .views import UserListCreateView, UserRetrieveUpdateDestroyAPIView, UserParkCreateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view(), name='user_retrieve_update_destroy'),
    path('/<int:pk>/create_park', UserParkCreateView.as_view(), name='user_create_park'),
]
