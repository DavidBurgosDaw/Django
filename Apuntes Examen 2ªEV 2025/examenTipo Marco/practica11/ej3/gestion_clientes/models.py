from django.db import models

class Usuario(models.Model):
    nickname = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    perfil = models.CharField(max_length=50)  # 'admin' o 'normal'

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    ciudad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15) 
    email = models.EmailField(max_length=50)
