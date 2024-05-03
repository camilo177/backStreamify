from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from myApp.models import Contenido

class ReadInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        contenido = Contenido.objects.all()
        return Response(contenido.values(), status=status.HTTP_200_OK)