from django.shortcuts import render
from .models import Producto
from .models import Profesor
from .models import Estudiante
from .models import Entregable
import datetime
# Create your views here.

def fecha_actual(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "fecha_actual.html", {"fecha_actual" : fecha_actual})

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, "producto_list.html", {"productos" : productos})

def profesor(request):
    profesor = Profesor.objects.all()
    return render(request,"profesor.html", {"profesor" : profesor})

def estudiante(request):
    estudiante = Estudiante.objects.all()
    return render(request,"estudiante.html", {"estudiante" : estudiante})

def entregables(request):
    entregables = Entregable.objects.all()
    return render(request,"entregables.html", {"entregables" : entregables})

def inicio(request):
    return render(request, "padre.html")