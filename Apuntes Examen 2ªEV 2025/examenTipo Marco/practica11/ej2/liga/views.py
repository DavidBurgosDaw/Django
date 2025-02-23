# views.py
from django.shortcuts import render, redirect
from .forms import PartidoForm
from .models import Equipo, Partido

def registrar_partido(request):
    if request.method == 'POST':
        form = PartidoForm(request.POST)
        if form.is_valid():
            partido = form.save()  # Guardamos el partido en la BD
            
            # Obtener los equipos
            equipo_casa = partido.equipo_casa
            equipo_visita = partido.equipo_visita

            # Lógica para actualizar puntos
            if partido.goles_casa > partido.goles_visita:
                equipo_casa.puntos += 3  # Victoria para equipo de casa
            elif partido.goles_casa < partido.goles_visita:
                equipo_visita.puntos += 3  # Victoria para equipo visitante
            else:
                equipo_casa.puntos += 1  # Empate
                equipo_visita.puntos += 1  

            # Guardamos los cambios en los equipos
            equipo_casa.save()
            equipo_visita.save()

            return redirect('lista_partidos')  # Redirige a la lista de partidos
    else:
        form = PartidoForm()  # Formulario vacío para GET

    return render(request, 'liga/registrar_partido.html', {'form': form})

def lista_equipos(request):
    equipos = Equipo.objects.all()  # Obtiene todos los equipos de la base de datos
    return render(request, 'liga/lista_equipos.html', {'equipos': equipos})

def lista_partidos(request):
    partidos = Partido.objects.all()  # Obtiene todos los partidos
    return render(request, 'liga/lista_partidos.html', {'partidos': partidos})
