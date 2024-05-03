from myApp.models import Production
from rest_framework import serializers
from myApp.models import VerProduction

class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = '__all__'


class VerProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerProduction
        fields = '__all__'


