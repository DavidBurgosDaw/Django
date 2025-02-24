from django.db import models

class Solicitud(models.Model):
    dni = models.CharField(max_length=9,  primary_key=True)
    provincia = models.CharField(max_length=100)
    renta = models.FloatField()
    edad = models.IntegerField()
    puntuacion = models.IntegerField()

class Usuario(models.Model):
    usuario = models.CharField(max_length=50,  primary_key=True)
    password = models.CharField(max_length=100)  
