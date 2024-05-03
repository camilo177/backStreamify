from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myApp.serializer import VerProductionSerializer

class CreateProductionView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = VerProductionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

