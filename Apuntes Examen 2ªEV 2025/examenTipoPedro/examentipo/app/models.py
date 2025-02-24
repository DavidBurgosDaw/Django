from django.db import models

# Create your models here.
class Laboratorio(models.Model):
    nombre_lab = models.CharField(max_length = 10, primary_key=True)
    num_ordenadores = models.IntegerField()
    email_tecnico = models.EmailField(max_length=50)
    
class Profesor(models.Model):
    nombre_completo = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.SET_NULL, null=True, blank=True)
    '''
        on_delete=models.SET_NULL	Si el laboratorio se borra, este campo se pone en NULL.
        null=True	Permite que el campo almacene valores NULL en la base de datos.
        blank=True	Permite que el campo se deje en blanco en formularios de Django.
    '''

class Incidencia(models.Model):
    numero = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    numero_ordenador = models.CharField(max_length = 10)
    descripcion = models.TextField()
    profesor = models.ForeignKey(Profesor, on_delete = models.CASCADE)
    resuelta = models.BooleanField(default=False)

class Resolucion(models.Model):
    incidencia = models.OneToOneField(Incidencia, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete = models.CASCADE)
    fecha_resolucion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    