from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from myApp.models import Production
from myApp.serializer import ProductionSerializer

class UpdateInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        try:
            production = Production.objects.filter(pk=pk).update(**request.data)
            return Response(production, status=status.HTTP_200_OK)
        except Production.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        