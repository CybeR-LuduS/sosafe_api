from django.db import models


class Perro(models.Model):
    id_perro = models.AutoField(primary_key=True)
    cod_chip = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    perdido = models.BooleanField()
    fecha_perdido = models.DateField(blank=True, null=True)
    robado = models.BooleanField()
    fecha_robado = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.cod_chip
