

# Create your models here.
from django.db import models

# Asegúrate de que esta clase existe exactamente con este nombre
class BecaFP(models.Model):
    dni = models.CharField(max_length=9, primary_key=True)
    provincia = models.CharField(max_length=100)
    renta = models.DecimalField(max_digits=10, decimal_places=2)
    edad = models.PositiveIntegerField()
    puntuacion = models.IntegerField()

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)