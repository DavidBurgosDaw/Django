from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Usuario, Equipo, Partido
from django.db.models import Q
# Create your views here.

#Crea el formulario login y hace que lo demas funcione
def Login(request):
    mensaje = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            usuario = buscar_usuario(usuario,password)
            if usuario is None:
                mensaje = "Credenciales incorrectas"
            else:
                return redirect(Equipos) #Recordar la view se pasa sin comillas
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form, 'mensaje': mensaje})


#Comprueba que las credenciales sean correctas
def buscar_usuario(usuario,password):
    try:
        return Usuario.objects.get(usuario=usuario,password=password)
    except Usuario.DoesNotExist:
        return None

#Devuelve los equipos con sus datos
def Equipos(request):
    equipos = Equipo.objects.all()
    return render(request,"equipos.html",{"equipos":equipos})

def Mostrar_Equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    return render(request,"detallesEquipo.html",{"equipo":equipo})

def Mostrar_Partido(request, id):
    partidos = Partido.objects.filter(Q(equipo_casa_id=id) | Q(equipo_visitante_id=id))
    return render(request,"detallesPartido.html",{"partidos":partidos})