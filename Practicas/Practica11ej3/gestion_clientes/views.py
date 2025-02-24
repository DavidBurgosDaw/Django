from django.shortcuts import render,redirect

# Create your views here.

from .models import Usuario, Cliente
from.forms import LoginForm

def login(request):
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
                perfil = usuario.perfil
                return redirect("DatosCliente",perfil)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'mensaje': mensaje})

#Aqui muestro los datos
def Muestra_Datos(request,perfil):
    usuarios = Cliente.objects.all()
    return render(request,'MuestraDatos.html',{"clientes":usuarios,"perfil":perfil})


def buscar_usuario(usuario,password):
    try:
        return Usuario.objects.get(usuario=usuario,password=password)
    except Usuario.DoesNotExist:
        return None




