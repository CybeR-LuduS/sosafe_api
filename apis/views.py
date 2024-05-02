from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PerroSerializer
from .models import Perro


class PerroViewSet(viewsets.ModelViewSet):
    queryset = Perro.objects.all()
    
    serializer_class = PerroSerializer