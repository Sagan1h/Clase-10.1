from django.contrib import admin
from .models import Producto

from AppDesafio import models

admin.site.register(models.Producto)
admin.site.register(models.Profesor)
admin.site.register(models.Estudiante)
admin.site.register(models.Entregable)