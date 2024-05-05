from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PerroSerializer
from .models import Perro


class PerroViewSet(viewsets.ModelViewSet):
    queryset = Perro.objects.all()
    serializer_class = PerroSerializer

    def get_queryset(self):
        cod_chip = self.request.GET.get('cod_chip')
        if cod_chip:
            return Perro.objects.filter(cod_chip=cod_chip)
        return self.queryset