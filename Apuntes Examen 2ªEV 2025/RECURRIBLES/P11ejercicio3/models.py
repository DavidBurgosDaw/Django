from django.db import models

class Usuario(models.Model):
    PERFIL_CHOICES = [
        ('normal', 'Normal'),
        ('administrador', 'Administrador'),
    ]
    usuario=models.CharField(max_length=50, unique=True)
    perfil = models.CharField(max_length=13, choices=PERFIL_CHOICES)
    password=models.CharField(max_length=50)


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
