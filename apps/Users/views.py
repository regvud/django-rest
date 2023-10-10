from rest_framework import generics

from apps.Users.models import UsersModel
from apps.Users.serializers import UsersSerializer


class UsersListCreateView(generics.ListCreateAPIView):
    queryset = UsersModel.objects.all()
    serializer_class = UsersSerializer


class UsersRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsersModel
    serializer_class = UsersSerializer
