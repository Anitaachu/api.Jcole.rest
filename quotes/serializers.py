from rest_framework import serializers 
from .models import Cole




class ColeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cole
        fields = "__all__"
