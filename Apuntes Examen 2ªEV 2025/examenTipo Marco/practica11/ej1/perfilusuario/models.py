from django.db import models

# Create your models here.
class Usuario(models.Model):
    #id = models.AutoField(primary_key=True)  # ID autoincremental como clave primaria
    nickname=models.CharField(max_length=50, primary_key=True)
    password =models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    telefono = models.CharField(max_length=15) 
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ultimo_acceso = models.DateTimeField(auto_now=True)
