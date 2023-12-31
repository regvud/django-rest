from rest_framework import generics
from rest_framework.response import Response

from apps.auto_parks.serializers import AutoParkSerializer
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer

from core.pagination import PagePagination


# Create your views here.
class UserListCreateView(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel
    serializer_class = UserSerializer


class UserParkCreateView(generics.GenericAPIView):
    queryset = UserModel.objects.all()

    def post(self, *args, **kwargs):
        data = self.request.data
        user = self.get_object()
        serializer = AutoParkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data, status=201)
