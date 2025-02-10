from django.db import IntegrityError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from gestion_alumnos.forms import FrmAlumno,FrmbuscarAlumno
from gestion_alumnos.models import Alumno

def home(request):
    return render(request,'base.html')

#Vista operaciones BBDD
@csrf_exempt
def anyadir(request):
    if request.method=='POST':
        my_frm=FrmAlumno(request.POST)
        if my_frm.is_valid():
            alumno=crear_alumno(my_frm) #FUNCIÓN DE UTILIDAD MÁS ABAJO
            try:
                alumno.save()    
                mensaje='Alumno añadido'
            except IntegrityError :  
                mensaje='Alumno no añadido'
            return render(request,'base.html',{'mensaje':mensaje})
    else:
        my_frm=FrmAlumno()
    return render(request,'anyadir.html',{'form':my_frm,'operacion':'add'})

@csrf_exempt    
def eliminar(request):
    if request.method=='POST':
        alumno=buscar_dni(request)
        if alumno is None:
             mensaje="Alumno no encontrado"
        else:
            alumno.delete()
            mensaje='Alumno eliminado'
        return render(request,'base.html',{'mensaje':mensaje})
    else:
        my_frm=FrmbuscarAlumno()    
    return render(request,'buscar.html',{'form':my_frm,'operacion':'delete'})    


@csrf_exempt    
def buscar(request):
    if request.method=='POST':
        alumno=buscar_dni(request)
        if alumno is None:
            mensaje="Alumno no encontrado"
            return render(request,'base.html',{'mensaje':mensaje})
        else:
            my_frm=FrmAlumno()
            my_frm.fields['nombre'].initial=alumno.nombre
            my_frm.fields['email'].initial=alumno.email
            my_frm.fields['nota'].initial=alumno.nota
            my_frm.fields['dni'].initial=alumno.dni
            my_frm.fields['dni'].widget.attrs['readonly']=True
            my_frm.fields['nombre'].widget.attrs['readonly']=True
            return render(request,'anyadir.html',{'form':my_frm,'operacion':'update'})
    else:
        my_frm=FrmbuscarAlumno()
    return render(request,'buscar.html',{'form':my_frm,'operacion':'search'})

@csrf_exempt    
def modificar(request):
    if request.method=='POST':
        my_frm=FrmAlumno(request.POST)
        if my_frm.is_valid():
            alumno=buscar_dni(request)
            alumno.email=my_frm.cleaned_data['email']
            alumno.nota=my_frm.cleaned_data['nota']
            alumno.save()
            return render(request,'base.html',{'mensaje':'Alumno modificado'})        
    else:
        my_frm=FrmAlumno()
    return render(request,'buscar.html',{'form':my_frm,'operacion':'search'})

def listado(request):
    lista_alumnos=Alumno.objects.all()
    return render(request,'listar.html',{'lista':lista_alumnos})
  
def listado_aprobados(request):
    lista_alumnos=Alumno.objects.filter(nota__gte=5)
    return render(request,'listar.html',{'lista':lista_alumnos})

@csrf_exempt    
def detalle_alumno(request,numero):
        alumno=buscar_numero(numero)
        datos={'a':alumno}
        return render(request,'detalle.html',datos)
    
#Funciones de utilidad   
def buscar_dni(request):
   my_frm=FrmbuscarAlumno(request.POST)
   if my_frm.is_valid():
        dni=my_frm.cleaned_data['dni']
        try:
            alumno=Alumno.objects.get(dni=dni)
        except Alumno.DoesNotExist:
                return None
        else:
            return alumno

def buscar_numero(numero):
    alumno=Alumno.objects.get(numero=numero)
    return alumno

def crear_alumno(frm:FrmAlumno):
    nombre=frm.cleaned_data['nombre']
    email=frm.cleaned_data['email']
    dni=frm.cleaned_data['dni']
    nota=frm.cleaned_data['nota']
    alumno=Alumno(nombre=nombre,email=email,dni=dni,nota=nota)
    #al=Alumno.objects.create(nombre=nombre,email=email,dni=dni,nota=nota)
    return alumno