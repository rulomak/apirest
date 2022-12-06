from .models import Project
from .serializers import ProjectSerializer
from rest_framework import viewsets, permissions

class ProjectViewset(viewsets.ModelViewSet):    
    queryset = Project.objects.all()  # todos los dato 
    permission_classes = [permissions.AllowAny]  # quien puede acceder a estos datos  ( filtrar mas adelante  )
    serializer_class =  ProjectSerializer
    
