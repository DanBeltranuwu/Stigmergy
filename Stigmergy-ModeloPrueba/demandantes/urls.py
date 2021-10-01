from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.demandantesCorporativos_view, name= 'demandantesCorporativos_view')
]