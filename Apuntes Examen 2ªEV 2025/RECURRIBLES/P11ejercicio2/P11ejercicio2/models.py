from django.db import models

class Equipo(models.Model):
    identificador = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=50)
    fecha_fundacion = models.DateTimeField()  # Remove auto_now_add if you want to set it manually
    victorias = models.IntegerField()  # Change to IntegerField for storing numbers



class Partido(models.Model):
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_visitante')
    identificador = models.CharField(max_length=50)  # Store the identificador of the team
    goles_local = models.IntegerField()
    goles_visitante = models.IntegerField()
