from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from myApp.models import Production
from myApp.serializer import ProductionSerializer

class UpdateInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        try:
            production = Production.objects.get(pk=pk)
        except Production.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductionSerializer(production, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)