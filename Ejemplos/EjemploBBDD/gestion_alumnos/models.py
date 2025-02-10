from django.db import models
from django.db.models.fields import CharField, DecimalField, EmailField


# Create your models here.
class Alumno(models.Model):
    nombre=models.CharField(max_length=80)
    dni=models.CharField(unique=True,max_length=9)
    email=models.EmailField(max_length=50)
    nota=models.DecimalField(max_digits=4,decimal_places=2)
    numero=models.AutoField(primary_key=True)
    