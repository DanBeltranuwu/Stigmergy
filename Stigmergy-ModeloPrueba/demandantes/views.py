from django.shortcuts import render
from .logic.demandantes_logic import get_DemandantesCorporativos
from django.core import serializers
from django.http import HttpResponse

def demandantesCorporativos_view(request):
    if request.method == 'GET':
        demandentesCorporativos = get_DemandantesCorporativos()
        demCorp_dto = serializers.serialize('json', demandentesCorporativos)
        return HttpResponse(demCorp_dto, 'application/json')