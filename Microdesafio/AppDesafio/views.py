from django.shortcuts import render
from .models import Producto
from .models import Profesor
from .models import Estudiante
from .models import Entregable
from .models import Curso
from .forms import CursoFormulario
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

def cursos_formulario(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) # Aca es donde nos llega la informacion del HTML
        print(mi_formulario)
        
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            curso = Curso(informacion["curso"], informacion["camada"])
            curso.save()
            return render(request, "padre.html")
    else:
        mi_formulario = CursoFormulario()
        return render(request, "cursos_formulario.html", {"mi_formulario" : mi_formulario})