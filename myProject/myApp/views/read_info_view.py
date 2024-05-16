import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from myApp.models import Production
from myApp.serializer import ProductionSerializer


class ReadInfoView(APIView):
    def get(self, request, *args, **kwargs):
        production = Production.objects.all()
        serializer = ProductionSerializer(production, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
              