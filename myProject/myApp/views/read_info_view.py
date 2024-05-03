import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from myApp.models import Production
from myApp.serializer import ProductionSerializer

class ReadInfoView(APIView): #Con el método get