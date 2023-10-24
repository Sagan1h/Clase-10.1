from django.urls import path
from . import views

urlpatterns = [
    path('fecha_actual/', views.mostrar_fecha_actual, name="mostrar_fecha_actual"),
    path('producto/', views.producto_list, name= "producto_list"),
    path('index/', views.index, name= "index"),
]