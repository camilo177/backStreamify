from myApp.models import Production
from rest_framework import serializers

class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = '__all__'