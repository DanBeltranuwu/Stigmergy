from django.db import models

class Demandante(models.Model):

    nombre = models.CharField(max_length=50)
    latitud = models.FloatField
    longitud = models.FloatField

    class Meta:
        abstract = True

class DemandanteCorporativo(Demandante):
    tipo = models.CharField(max_length=50)
    nit = models.CharField(max_length=50)

class DemandantePersonal(Demandante):
    apellido = models.CharField(max_length=50)
    identificacion = models.FloatField