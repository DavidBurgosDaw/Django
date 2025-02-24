from django.shortcuts import render, redirect
from gestion.forms import *
from gestion.models import *
from django.db import IntegrityError

# Create your views here.
def Login(request):
    errorMessage=""
    
    #httpPOST
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            usuario = getUsuarioByEmail(email)
            if usuario is None:
                errorMessage="Usuario no registrado"
            elif usuario.password != password:
                errorMessage="Credenciales incorrectas"
            else:
                if usuario.laboratorio:
                    return redirect('tecnico', email)
                else:
                    return redirect('profesor', email)
    #httpGET
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form,'mensaje':errorMessage})

def getUsuarioByEmail(email):
    try:
        return Profesor.objects.get(email=email)
    except Profesor.DoesNotExist:
        return None
    
def ProfesorView(request,email):
    mensaje=""
    profesor=getUsuarioByEmail(email)
    if request.method=="POST":
        form=AltaForm(request.POST)
        if form.is_valid():
            try:
                profesor=Profesor.objects.get(email=email)
                laboratorioNombre=form.cleaned_data['laboratorio']
                laboratorio=Laboratorio.objects.get(nombre_lab=laboratorioNombre)
                numero_ordenador='PC'+form.cleaned_data['numPc']
                descripcion=form.cleaned_data['descripcion']
                incidencia=Incidencia(profesor=profesor,numero_ordenador=numero_ordenador,descripcion=descripcion,laboratorio=laboratorio,resuelta=False)
                incidencia.save()
                mensaje="Incidencia añadida correctamente"
                form=AltaForm()
            except IntegrityError:
                mensaje='Incidencia no ha podido ser añadida a la BBDD'
        return render(request,'profesor.html',{'form':form,'mensaje':mensaje,'email':email})
    else:
        form=AltaForm()
    return render(request,'profesor.html',{'form':form,'mensaje':mensaje,'email':email})

def TecnicoView(request,email):
    tecnico=getUsuarioByEmail(email)
    incidencias= Incidencia.objects.all()
    return render(request,'tecnico.html',{'incidencias':incidencias})

def Detalles(request, numero):
    incidencia=Incidencia.objects.get(numero=numero)
    form = AltaForm(initial={
            'laboratorio': incidencia.laboratorio,  
            'numPc': incidencia.numero_ordenador,  
            'descripcion': incidencia.descripcion
        })
    return render(request, 'detalles.html',{'form':form,'email':incidencia.laboratorio.email_tecnico})

def Resolver(request, numero):
    mensaje=""
    if request.method=='POST':
        form=AltaForm(request.POST)
        if form.is_valid():
            try:
                incidencia=Incidencia.objects.get(numero=numero)
                incidencia.descripcion+=form.cleaned_data['descripcion']
                incidencia.resuelta=True
                incidencia.save()
                
                return redirect('tecnico',email=incidencia.laboratorio.email_tecnico)
            except IntegrityError:
                mensaje='Incidencia no actializada'
            
    else:
        incidencia=Incidencia.objects.get(numero=numero)
        form = AltaForm(initial={
                'laboratorio': incidencia.laboratorio,  
                'numPc': incidencia.numero_ordenador,  
                'descripcion': incidencia.descripcion,
            })
    return render(request, 'resolver.html',{'form':form,'email':incidencia.laboratorio.email_tecnico,'mensaje':mensaje})