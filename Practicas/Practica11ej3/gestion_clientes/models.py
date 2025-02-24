from django.db import models

class Usuario(models.Model):
    PERFIL_CHOICES = [
        ('admin', 'Administrador'),
        ('normal', 'Normal'),
    ]

    usuario = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)  # Guardar encriptada
    perfil = models.CharField(max_length=10, choices=PERFIL_CHOICES, default='normal')

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=100, unique=True)  