from django.shortcuts import render
from .models import Producto
import datetime
# Create your views here.

def mostrar_fecha_actual(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "fecha_actual.html", {"fecha_actual" : fecha_actual})

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, "producto_list.html", {"productos" : productos})

def index(request):
    return render(request, "index.html")