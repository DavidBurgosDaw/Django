from django.shortcuts import render
from ListaAsignaturas.Models.Asignatura import Asignatura  # Nombre corregido
# Create your views here.

def asignaturas(request):
    x = [
        Asignatura(nombre="Aplicaciones Web", profesor="Rosa", numero=103, hSemanales=8, imagen="daw.jpg"),
        Asignatura(nombre="Sistemas Informáticos", profesor="Luis Palazuelo", numero=104, hSemanales=6, imagen="asir.jfif"),
        Asignatura(nombre="Despliegue de Aplicaciones Web", profesor="Eva Moya", numero=105, hSemanales=4, imagen="despliegue.jpg")
    ]
    
    return render(request, "asignaturas.html", {"asignaturas": x})
