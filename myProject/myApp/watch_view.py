from rest_framework.views import APIView
from rest_framework.response import Response
from myApp.models import VerProduction
from myApp.serializer import VerProductionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class VerProductionView(APIView):
    def get(self, request):
        productions = VerProduction.objects.all().order_by('-popularity')
        serializer = VerProductionSerializer(productions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
