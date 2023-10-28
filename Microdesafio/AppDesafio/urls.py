from django.urls import path
from . import views

urlpatterns = [
    path('fecha_actual/', views.fecha_actual, name="fecha_actual"),
    path('productos/', views.producto_list, name= "producto_list"),
    path('profesor/', views.profesor, name= "profesor"),
    path('estudiante/', views.estudiante, name= "estudiante"),
    path('entregables/', views.entregables, name= "entregables"),
    path('', views.inicio, name= "inicio"),
]