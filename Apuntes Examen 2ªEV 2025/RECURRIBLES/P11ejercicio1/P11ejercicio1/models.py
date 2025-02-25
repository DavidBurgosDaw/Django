from django.db import models
class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_UltAcc = models.DateTimeField()
    password = models.CharField(max_length=50)


    
    