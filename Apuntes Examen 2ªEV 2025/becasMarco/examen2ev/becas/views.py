from django.shortcuts import render, redirect
from becas.forms import SolicitudForm, ConsultaForm, LoginForm
from becas.models import Solicitud, Usuario
from django.db import IntegrityError

# Create your views here.
def Home(request):
    return render(request, 'becas/base.html', {})

def solicitar_beca(request):
    mensaje = ""

    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            provincia = form.cleaned_data['provincia'].capitalize()
            renta = form.cleaned_data['renta']
            edad = form.cleaned_data['edad']
            solicitudExiste = buscar_solicitud(dni)

            if solicitudExiste is None:
                puntuacion = calcular_puntuacion(provincia, renta, edad)

                try:
                    solicitud = form.save(commit=False) 
                    solicitud.provincia = provincia
                    solicitud.puntuacion = puntuacion  
                    solicitud.save()
                    return redirect('home') #volver a la a pagina principal
                except IntegrityError:  
                    mensaje = 'Incidencia no ha podido ser añadida a la BBDD'
            
            else:
                mensaje = "Solicitud ya existente"

    else:
        form = SolicitudForm()

    return render(request, 'becas/solicitar_beca.html', {'form': form, 'mensaje': mensaje})

def calcular_puntuacion(provincia, renta, edad):
    puntuacion = 0
    if provincia.lower() == "madrid":
        puntuacion += 1
    if renta < 6000:
        puntuacion += 2
    elif 6000 <= renta <= 10000:
        puntuacion += 1
    if edad > 21:
        puntuacion += 2
    return puntuacion

def buscar_solicitud(dni):
    try:
        return Solicitud.objects.get(dni=dni)
    except Solicitud.DoesNotExist:
        return None

def ver_beca(request):
    mensaje = ""

    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            solicitudExiste = buscar_solicitud(dni)

            if solicitudExiste is None:
                mensaje = "No existe solicitud para este dni"
            else:
                return redirect('info_beca', dni)  # pasamos dni

    else:
        form = ConsultaForm()

    return render(request, 'becas/ver_beca.html', {'form': form, 'mensaje': mensaje})

def info_beca(request, dni):
    solicitud = buscar_solicitud(dni)
    return render(request, 'becas/info_beca.html', {'solicitud': solicitud})

def login(request):
    mensaje = ""

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']

            usuario = buscar_usuario(usuario)

            if usuario is None:
                mensaje = "Usuario no encontrado"
            elif usuario.password != password:
                mensaje = "Contraseña incorrecta"
            else:
                return redirect('mostrar_lista')

    else:
        form = LoginForm()

    return render(request, 'becas/login.html', {'form': form, 'mensaje': mensaje})

def buscar_usuario(usuario):
    try:
        return Usuario.objects.get(usuario=usuario)
    except Usuario.DoesNotExist:
        return None

def mostrar_lista(request):
    mensaje = ""
    solicitudes = buscar_solicitudes()
    if not solicitudes:
        mensaje = "No se han encontrado solicitudes"
    return render(request, 'becas/mostrar_lista.html', {'solicitudes': solicitudes, 'mensaje': mensaje})

def buscar_solicitudes():
    try:
        return Solicitud.objects.all()
    except Solicitud.DoesNotExist:
        return None
