# models.py
from django.db import models

class Equipo(models.Model):
    nombre_completo = models.CharField(max_length=100)
    identificador = models.CharField(max_length=20, unique=True)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre_completo

class Partido(models.Model):
    equipo_casa = models.ForeignKey(Equipo, related_name='partidos_casa', on_delete=models.CASCADE)
    goles_casa = models.IntegerField()
    equipo_visita = models.ForeignKey(Equipo, related_name='partidos_visita', on_delete=models.CASCADE)
    goles_visita = models.IntegerField()

    def __str__(self):
        return f"{self.equipo_casa.nombre_completo} vs {self.equipo_visita.nombre_completo}"