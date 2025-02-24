from django.db import models

# Create your models here.

class Laboratiorio(models.Model):
    nombre = models.CharField(max_length=30)
    numero_ordenadores = models.IntegerField()
    email_tecnico = models.EmailField(max_length=30)

class Profesor(models.Model):
    nombre_completo = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=128)
    laboratorio = models.ForeignKey(Laboratiorio, on_delete=models.SET_NULL, null=True, blank=True)
    '''
        on_delete=models.SET_NULL	Si el laboratorio se borra, este campo se pone en NULL.
        null=True	Permite que el campo almacene valores NULL en la base de datos.
        blank=True	Permite que el campo se deje en blanco en formularios de Django.
    '''

class Incidencia(models.Model):
    numero_inc = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    laboratorio = models.ForeignKey(Laboratiorio, on_delete=models.CASCADE)
    numero_ordenador = models.IntegerField()
    descripcion = models.TextField()
    email_profesor = models.EmailField(max_length=30)
    resuelta = models.BooleanField(default=False)

class Resolucion(models.Model):
    numero_inc = models.IntegerField()
    email_profesor = models.EmailField()
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()

    