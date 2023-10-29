from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio =  models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=100)

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    mail = models.EmailField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    mail = models.EmailField()
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    entreado = models.BooleanField()

class Curso(models.Model):
    curso = models.CharField(max_length=100)
    camada = models.IntegerField()