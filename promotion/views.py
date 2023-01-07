from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class Welcome(APIView):
    @staticmethod
    def get(request):
        return Response({'message': 'I am Alive'}, status.HTTP_200_OK)
