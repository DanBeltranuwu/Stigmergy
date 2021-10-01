from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .logic.ordenes_logic import update_estadoOrden_by_pk

def update_estado(request, pk, estado):
    orden = update_estadoOrden_by_pk(pk, estado)
    orden_list = serializers.serialize('json', orden)
    return HttpResponse(orden_list, content_type = 'application/json')
