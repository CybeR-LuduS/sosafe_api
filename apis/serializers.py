from rest_framework import serializers

from .models import Perro

class PerroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perro
        fields = ('id_perro', 'cod_chip', 'nombre', 'perdido', 'fecha_perdido', 'robado', 'fecha_robado')