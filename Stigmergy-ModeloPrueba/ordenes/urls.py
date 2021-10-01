from django.urls import path
from . import views

urlpatterns = [
    path('update/<int:pk>-<estado>', views.update_estado, name='update-estado')
]