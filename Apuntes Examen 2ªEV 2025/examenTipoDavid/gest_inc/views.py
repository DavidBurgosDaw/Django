from django.shortcuts import render, redirect
from .models import Profesor,Laboratiorio,Incidencia,Resolucion
from .forms import loginForm, AltaForm
# Create your views here.

def login(request):
    mensaje = ""
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            usuario = buscar_profesor(email,password)
            if usuario is None:
                mensaje = "Credenciales incorrectas"
            else:
               if usuario.laboratorio is None:
                   return redirect('profesor',email)
               else:
                    return redirect('tecnico',email)
    else:
        form = loginForm()
    return render(request, 'login.html', {'form': form, 'mensaje': mensaje})

def buscar_profesor(email,password):
    try:
        return Profesor.objects.get(email=email)
    except Profesor.DoesNotExist:
        return None
    

def vista_profesor(request,email):
    mensaje = ""
    if request.method == 'POST':
        form = AltaForm(request.POST)
        if form.is_valid():
            email = email
            laboratorio = form.cleaned_data['laboratorio']
            numPc = form.cleaned_data['numPc']
            descripcion =  form.cleaned_data['descripcion']
            nueva_inc = Incidencia(numero_ordenador=numPc,descripcion=descripcion,email_profesor=email,laboratorio_id =laboratorio)
            nueva_inc.save()
            return render(request, 'profesor.html', {'form': form, 'mensaje': mensaje,'email':email})
    else:
        form = AltaForm()
    return render(request, 'profesor.html', {'form': form, 'mensaje': mensaje,'email':email})

def vista_tecnico(request,email):
    tecnico = Profesor.objects.get(email=email)
    incidencias = Incidencia.objects.filter(laboratorio=tecnico.laboratorio)
    return render(request, 'tecnico.html', {'incidencias': incidencias, 'email': email})
