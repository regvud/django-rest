from rest_framework import generics
from rest_framework.response import Response

from apps.auto_parks.serializers import AutoParkSerializer
from apps.Users.models import UsersModel
from apps.Users.serializers import UsersSerializer


class UsersListCreateView(generics.ListCreateAPIView):
    queryset = UsersModel.objects.all()
    serializer_class = UsersSerializer


class UsersRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsersModel
    serializer_class = UsersSerializer


class UsersAutoParksCreateView(generics.GenericAPIView):
    queryset = UsersModel.objects.all()

    def get(self, *args, **kwargs):
        user = self.get_object()
        serializer = UsersSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return print(user)

    def post(self, *args, **kwargs):
        data = self.request.data
        user = self.get_object()
        serializer = AutoParkSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

        return Response(serializer.data, status=201)
