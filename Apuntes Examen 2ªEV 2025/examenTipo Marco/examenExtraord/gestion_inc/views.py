from django.shortcuts import render, redirect
from gestion_inc.forms import LoginForm, AltaIncidenciaForm
from gestion_inc.models import Profesor, Laboratorio, Incidencia, Resolucion
from django.db import IntegrityError
# Create your views here.

def Login(request):
    mensaje = ""

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            usuario = buscar_usuario(email)

            if usuario is None:
                mensaje = "Usuario no encontrado"
            elif usuario.password != password:  
                mensaje = "Contraseña incorrecta"
            else:
                if usuario.laboratorio:
                    return redirect('tecnico', email) #si tiene lab es un tecnico que gestiona incidencias
                else:
                    return redirect('profesor', email) #si no tiene ningun laboratio es un profesor que quiere dar de alta incidencias

    else:
        form = LoginForm()

    return render(request, 'gestion_inc/login.html', {'form': form, 'mensaje': mensaje})

def buscar_usuario(email):
    try:
        return Profesor.objects.get(email=email)
    except Profesor.DoesNotExist:
        return None
    
def Profesor_View(request, email):
    mensaje = ""
    profesor = buscar_usuario(email)  # Obtener el profesor que hizo login

    if request.method == 'POST':
        form = AltaIncidenciaForm(request.POST)
        if form.is_valid():
            try:
                incidencia = form.save(commit=False)  # No guarda aún en la base de datos
                incidencia.profesor = profesor  # Asignar el profesor a la incidencia
                incidencia.save()  # Ahora sí, guardar en la base de datos
                mensaje = "Incidencia añadida correctamente."
                
                # Aquí estamos creando un nuevo formulario vacío
                form = AltaIncidenciaForm()#para mostrar en la vista de forma vacia

            except IntegrityError :  
                mensaje='Incidencia no ha podido ser añadida a la BBDD'
            
            return render(request, 'gestion_inc/profesor.html', {'form': form, 'mensaje': mensaje, 'email': email})
    else:
        form = AltaIncidenciaForm()

    return render(request, 'gestion_inc/profesor.html', {'form': form, 'mensaje': mensaje, 'email': email})


def Tecnico_View(request, email):
    tecnico = Profesor.objects.get(email=email)
    incidencias = Incidencia.objects.filter(laboratorio=tecnico.laboratorio)

    return render(request, 'gestion_inc/tecnico.html', {'incidencias': incidencias, 'email': email})

def resolver_incidencia(request, numero):
    incidencia = Incidencia.objects.get(numero=numero)
    incidencia.resuelta = True  # Marca la incidencia como resuelta
    incidencia.save()

    return redirect('tecnico', email=incidencia.laboratorio.email_tecnico)  # Redirige al técnico a la vista de incidencias

def detalles_incidencia(request, numero):
    incidencia = Incidencia.objects.get(numero=numero)
    
    return render(request, 'gestion_inc/detalles_incidencia.html', {'incidencia': incidencia})