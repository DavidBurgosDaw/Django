from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, primary_key=True)
    telefono = models.CharField(max_length=9)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ultimo_acceso = models.DateTimeField(null=True, blank=True)

class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    identificador = models.CharField(max_length=20, null=False)
    nombre = models.CharField(max_length=30)
    num_jugadores = models.IntegerField(validators=[MaxValueValidator(20)])
