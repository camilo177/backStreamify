# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from myApp.models import PerfilAdministrador
from django.db import IntegrityError

class CreateAdminProfileView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create a new user
            usuario = User.objects.create_user(username=username, password=password)
            # Create an admin profile associated with the user
            perfil = PerfilAdministrador.objects.create(user=usuario)
            return Response({"mensaje": "Perfil de administrador creado correctamente"}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
