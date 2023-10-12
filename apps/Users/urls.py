from django.urls import path

from apps.Users.views import UsersAutoParksCreateView, UsersListCreateView, UsersRetrieveUpdateDestroyView

urlpatterns = [
    path('', UsersListCreateView.as_view(), name='users_list_create'),
    path('/<int:pk>', UsersRetrieveUpdateDestroyView.as_view(), name='users_retrieve_update_destroy'),
    path('/<int:pk>/auto_parks', UsersAutoParksCreateView.as_view(), name='users_create_auto_park_by_id'),

]
