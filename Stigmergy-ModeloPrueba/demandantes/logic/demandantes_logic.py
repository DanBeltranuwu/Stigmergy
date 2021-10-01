from ..models import DemandanteCorporativo

def get_DemandantesCorporativos():
    demandantesCorporativos = DemandanteCorporativo.objects.all()
    return demandantesCorporativos