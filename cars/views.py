from rest_framework.response import Response
from rest_framework.views import APIView


class CarsView(APIView):
    def get(self, *args, **kwargs):
        print(self.request.query_params.dict())
        return Response('get response')
