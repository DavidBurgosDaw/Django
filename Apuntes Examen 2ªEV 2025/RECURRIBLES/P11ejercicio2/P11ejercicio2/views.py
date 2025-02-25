from .models import Equipo,Partido
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def info(request):
    equipos=Equipo.objects.all()
    print(equipos)
    return render(request,'info.html',{'equipos':equipos})

def verEquipo(request, identificador):
    try:
        equipo = Equipo.objects.get(identificador=identificador)
        return render(request,'verEquipo.html', {'equipo': equipo})
    except Equipo.DoesNotExist:
        mensaje="Equipo no encontrado"
        return render(request,"login.html",{"mensaje",mensaje})
    
def datosPartido(request,identificador):
    try:
        l_partidos = Partido.objects.filter(identificador=identificador)
        
        return render(request,'verPartidos.html', {'l_partidos': l_partidos})
    except Partido.DoesNotExist:
        mensaje="Equipo no encontrado"
        return render(request,"login.html",{"mensaje",mensaje})