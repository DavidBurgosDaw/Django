from django.shortcuts import render,redirect
from app.forms import *
from app.models import *
from django.db import IntegrityError
from datetime import datetime


# Create your views here.
def home(request):
    mensaje = ""
    if request.method=='POST':
        frm=FrmLogin(request.POST)
        if frm.is_valid():
            email = frm.cleaned_data['email']
            password = frm.cleaned_data['password']
            usuario = buscar_usuario(email)
            print(usuario)
            if usuario is None:
                mensaje = "Usuario no encontrado"
            elif usuario.password != password:  
                mensaje = "Contraseña incorrecta"
            else:
                if usuario.laboratorio:
                    inci = Incidencia.objects.all()
                    return render(request,'tecnico.html',{'incidencia':inci,'usuario':usuario})
                else:
                    labs = Laboratorio.objects.all()
                    return render(request,'profesor.html',{'usuario':usuario,'labs':labs})
    else:
        frm=FrmLogin()
    return render(request,'form.html',{'form':frm,'mensaje':mensaje})

def buscar_usuario(email):
    try:
        return Profesor.objects.get(email=email)
    except Profesor.DoesNotExist:
        return None

def incidenciaLab(request, email):
    mensaje = ""
    # Buscar al usuario que reporta la incidencia
    usuario = buscar_usuario(email)
    if request.method == 'POST':
        frm = FrmIncidencia(request.POST)
        if frm.is_valid():
            try:
                # Crear la incidencia sin guardar aún
                incidencia = frm.save(commit=False)
                # Asignar el usuario que reporta la incidencia
                incidencia.profesor = usuario  # Suponiendo que la incidencia tiene un campo 'profesor'

                #Prueba quitar milisegundos
                #if incidencia.fecha:
                #    incidencia.fecha = incidencia.fecha.replace(microsecond=0)
                #else:
                #    incidencia.fecha = datetime.now().replace(microsecond=0)  # Asigna la fecha actual

                # Guardar en la base de datos
                incidencia.save()
                frm = FrmIncidencia()
            except IntegrityError:
                mensaje = 'Incidencia no ha podido ser añadida a la BBDD'
    else:
        frm = FrmIncidencia()
    return render(request, 'incidencias.html', {'form': frm, 'mensaje': mensaje, 'email': email})

def solIncidencia(request,numero,email):
    mensaje=""
    print(email)
    if request.method == 'POST':
        frm = FrmGestionarIncidencia(request.POST)
        if frm.is_valid():
            incidencia=getIncidencia(numero)
            if incidencia is None:
                mensaje="No existe incidencia"
            else:
                incidencia.resuelta=True
                incidencia.descripcion="Resuelto: "+incidencia.descripcion
                incidencia.save()
                return render(request,'cambio.html')
    else: 
        frm = FrmGestionarIncidencia()

#    else :
#        try:
#            incidencia =getIncidencia(numero)  
#            if incidencia is None :
#                mensaje = 'Incidencia no encontrada'   
#            else:
#                incidencia.fecha= datetime.now()
#                incidencia.resuelta=True
#        except IntegrityError:
#            mensaje = 'Incidencia no ha podido ser añadida a la BBDD'   
#
    return render(request,'incidencias.html',{'mensaje':mensaje,'email':email,'numero':numero,'form':frm})

def getIncidencia(numero):
    try:
        print(numero)
        print(Incidencia.objects.get(numero=numero))
        return Incidencia.objects.get(numero=numero)
    except Incidencia.DoesNotExist: 
        return None

def verincidencia(request,numero):
    incidencia=getIncidencia(numero)
    return render(request,'detallesIncidencias.html',{'incidencia':incidencia})