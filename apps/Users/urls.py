from django.urls import path

from apps.Users.views import UsersListCreateView, UsersRetrieveUpdateDestroyView

urlpatterns = [
    path('', UsersListCreateView.as_view(), name='users_list_create'),
    path('/<int:pk>', UsersRetrieveUpdateDestroyView.as_view(), name='users_retrieve_update_destroy')
]
