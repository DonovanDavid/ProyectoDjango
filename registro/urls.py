from django.urls import path
from . import views

urlpatterns = [
    path('' , views.consultaPersona),
    path('ciudades/' , views.consultaCiudades),
    path('tipoDocumento/' , views.consultaTipoDocumento),
    path('personas/' , views.consultaPersona),
    path('eliminarPersona/<int:id>', views.eliminarPersona, name= 'eliminarPersona'),
]