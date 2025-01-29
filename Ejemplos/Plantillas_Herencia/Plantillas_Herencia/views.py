
from django.shortcuts import render

from Plantillas_Herencia.models.asignatura import Asignatura

def home(request):
    return render(request, 'base_SECCIONASIGNATURA.html')

def servidor(request):
    asig=Asignatura("Desarrollo en entorno servidor","Rosa Rodríguez",8,"laboratorio 12")
    return render(request,'servidor_template.html',{"asignatura":asig})

def moviles(request):
    asig=Asignatura("Desarrollo de aplicaciones para dispositivos móviles","Rosa Rodríguez",4,"laboratorio 12")
    return render(request,'moviles_template.html',{"asignatura":asig})