from django.urls import path
from . import views

urlpatterns = [
    path('fecha_actual/', views.fecha_actual, name="fecha_actual"),
    path('productos/', views.producto_list, name= "producto_list"),
    path('inicio/', views.inicio, name= "inicio"),
]