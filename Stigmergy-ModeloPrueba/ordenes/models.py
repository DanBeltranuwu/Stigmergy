from django.db import models

from demandantes.models import Demandante

class Orden(models.Model):

    class TipoOrden(models.TextChoices):
        SINCONFIRMAR = 'SC', _('Sin Confirmar')
        CONFIRMADO = 'CN', _('Confirmado')
        ENPREPARACION = 'EP', _('En Preparación')
        LISTO =  'LS', _('Listo')
        ENCAMINO = 'EC', _('En camino')
        ENTREGADO = 'EN', _('Entregado')

    demandante = models.ForeignKey(Demandante, on_delete=models.CASCADE, default=None)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=2,
        choices= TipoOrden.choices,
        default= TipoOrden.SINCONFIRMAR,
    )
    valorTotal = models.FloatField

    def __str__(self):
        return '{}'.format(self.fecha)