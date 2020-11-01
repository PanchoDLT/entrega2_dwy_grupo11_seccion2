from django.contrib import admin
from django.urls import path, include
from .views import Pagina_inicio,galeria,Mapa,Quienes_somos,Registro_insumos,Registro,login,logout_vista

urlpatterns = [
    path('',Pagina_inicio, name='PAGINA_INICIO'),
    path('Galeria/',galeria,name='GALERIA'),
    path('Mapa/',Mapa,name='MAPA'),
    path('Quienes_somos/',Quienes_somos,name='QUIENES_SOMOS'),
    path('Registro_insumos/',Registro_insumos,name='REGISTRO_INSUMOS'),
    path('Registro/',Registro,name='REGISTRO'),
    path('login/',login,name='LOGIN'),
    path('logout_vista/',logout_vista,name='LOGOUT'),
]