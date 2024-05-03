from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myApp.models import Production

class DeleteInfoView(APIView):
    def delete(self, request, pk):
        try:
            contenido = Production.objects.get(id=pk)
            contenido.delete()
            return Response({"mensaje": "Contenido eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
        except Production.DoesNotExist:
            return Response({"error": "El contenido no existe"}, status=status.HTTP_404_NOT_FOUND)
        except:
            # Handle other exceptions like database errors or server errors
            return Response({"error": "Error interno del servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
