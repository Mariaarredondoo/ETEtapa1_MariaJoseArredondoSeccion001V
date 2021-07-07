from django.conf import urls
from django.urls import path 
from .views import index, registrar,ver_registros,modificar,eliminar

urlpatterns = [
    path('',index, name='index'),
    path('ver-registros',ver_registros,name='ver_registros'),
    path('registrar', registrar, name='registrar'),
    path('modificar/<id>',modificar, name='modificar'),
    path('eliminar<id>',eliminar,name='eliminar')
]