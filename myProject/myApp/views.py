from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class NominaView(APIView):
    def get(self, request, *args, **kwargs):
        horas = int(request.GET.get('horas', 0))
        tarifa = float(request.GET.get('tarifa', 0))
        trabajador = request.GET.get('trabajador', '')

        if horas <= 35:
            salario = horas * tarifa
        else:
            salario = (35 * tarifa) + ((horas - 35) * 1.5 * tarifa)

        if salario > 2000 and salario <= 2220:
            salario -= salario * 0.2
        elif salario > 2220:
            salario -= salario * 0.3

        return Response({'Salario de ' + trabajador + ' es': salario}, status=status.HTTP_200_OK)
