from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):  # crea un modelo que podra ser consultado 
    class Meta:
        model = Project   
        fields = ('id', 'title', 'description', 'technology', 'create_at')   # campos que podran ser consultados  
        read_only_fields = ('create_at', )  #  campo de solo lectura  (, al final ) tupla

        