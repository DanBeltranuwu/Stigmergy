from ..models import Orden

def update_estadoOrden_by_pk(num, estado):
    orden = Orden.objects.get(pk = num)
    orden.estado = estado
    orden.save()

    ordenes = Orden.objects.all()
    return ordenes