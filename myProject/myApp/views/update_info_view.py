from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myApp.models import Production
from myApp.serializer import ProductionSerializer
from django.shortcuts import get_object_or_404

class GetInfoView(APIView):

    def get(self, request, pk, *args, **kwargs):
        production = get_object_or_404(Production, pk=pk)
        serializer = ProductionSerializer(production)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateInfoView(APIView):

    def put(self, request, pk):
        try:
            production = Production.objects.get(pk=pk)  
            serializer = ProductionSerializer(production, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Production.DoesNotExist:
            return Response({"error": "Production not found"}, status=status.HTTP_404_NOT_FOUND)
