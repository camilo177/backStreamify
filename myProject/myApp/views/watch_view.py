from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myApp.models import VerProduction
from myApp.serializer import VerProductionSerializer

class WatchProductionView(APIView):
    def get(self, request,  *args, **kwargs):
        ver_productions = VerProduction.objects.all()
        serializer = VerProductionSerializer(ver_productions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)