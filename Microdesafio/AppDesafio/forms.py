from django import forms
from .models import Producto

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()