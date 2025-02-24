from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse  # ✅ Importar reverse
from depart_informatica.forms import FrmLogin,IncidenciaForm,ResolverIncidenciaForm, DetallesForm
from depart_informatica.models import Profesor, Laboratorio, Incidencia, Resolucion
from django.db import IntegrityError


def login(request):
    if request.method == 'POST':
        frm = FrmLogin(request.POST)
        if frm.is_valid():
            email = frm.cleaned_data['email']
            password = frm.cleaned_data['password']
            usuario = buscar_usuario(email)
            if usuario is None:
                messages.error(request, "Usuario no encontrado")
            elif usuario.password != password:  
                messages.error(request, "Contraseña incorrecta")
            else:
                if usuario.laboratorio:
                    return redirect(reverse('tecnico_view', args=[usuario.email]))
                else:
                    return redirect(reverse('profesor_view', args=[usuario.email]))  # ✅ Redirigir a profesor_view
    else:
        frm = FrmLogin()
    return render(request, 'login.html', {'form': frm})

def profesor_view(request, email):
    profesor = Profesor.objects.get(email=email)
    laboratorios = Laboratorio.objects.all()  # ✅ Obtener la lista de laboratorios
    return render(request, 'profesor.html', {'usuario': profesor, 'laboratorios': laboratorios})

def tecnico_view(request, email):
    tecnico = Profesor.objects.filter(email=email).first()
    incidencias = Incidencia.objects.filter(laboratorio=tecnico.laboratorio)
    return render(request, 'tecnico.html', {'incidencias': incidencias})

def buscar_usuario(email):
    try:
        return Profesor.objects.get(email=email)
    except Profesor.DoesNotExist:
        return None
    
def profesor_incidencia(request,email): #el email se tiene que llamar IGUAL al de la url 
    if request.method == 'POST':
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            profesor = Profesor.objects.get(email=email)  # Buscamos el profesor con este email
            laboratorio=form.cleaned_data['laboratorio']
            numero_ordenador= form.cleaned_data['numero_ordenador']
            descripcion = form.cleaned_data['descripcion']
            
            nueva_incidencia = Incidencia(
                laboratorio=Laboratorio.objects.get(nombre_lab=laboratorio),
                numero_ordenador=numero_ordenador,
                descripcion=descripcion,
                profesor=profesor
            )            
            try:
                nueva_incidencia.save()
                mensaje="Incidencia añadida"
            except IntegrityError :
                mensaje="Incidencia no añadida"
            return render(request,"incidencia_exito.html",{"mensaje":mensaje,"email":email})
    else:
        form = IncidenciaForm(initial={'email': email})

    return render (request, "profesor_incidencia.html",{"form":form})



def resolver(request, email, numero_incidencia):
    incidencia = Incidencia.objects.get(numero=numero_incidencia)  # Obtener la incidencia

    if request.method == "POST":
        descripcion_resolucion = request.POST.get("descripcion_resolucion")
        incidencia.resuelta = True
        incidencia.descripcion = descripcion_resolucion
        incidencia.save()
        return redirect("tecnico_view", email=email)  # Redirigir al técnico después de resolver

    return render(request, "resolver.html", {"incidencia": incidencia, "email": email})

def detalles(request,numero_incidencia):
    incidencia = Incidencia.objects.get(numero=numero_incidencia)
    return render(request, "detalle_incidencia.html", {"incidencia": incidencia})
