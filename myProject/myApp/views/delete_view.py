from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from myApp.models import Contenido

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff

class EliminarContenidoView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        try:
            contenido = Contenido.objects.get(pk=pk)
            contenido.delete()
            return Response({"mensaje": "Contenido eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
        except Contenido.DoesNotExist:
            return Response({"error": "El contenido no existe"}, status=status.HTTP_404_NOT_FOUND)
