from django.shortcuts import render,redirect

# Create your views here.

from .models import Usuario, Cliente
from.forms import LoginForm, RegisterForm

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




def Muestra_Datos(request, perfil):
    mensaje = ""
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            ciudad = form.cleaned_data['ciudad']
            
            cliente = buscar_cliente(email)
            if cliente is None:
                nuevo_cliente = Cliente(nombre=usuario, telefono=telefono, email=email, ciudad=ciudad)
                nuevo_cliente.save()
            else:
                mensaje = "El cliente ya existe"
        
        # Si el formulario no es válido o el cliente ya existe, se sigue aquí
        usuarios = Cliente.objects.all()
        return render(request, 'MuestraDatos.html', {
            "clientes": usuarios,
            "perfil": perfil,
            "form": form,
            "mensaje": mensaje
        })

    # Si el método es GET, mostramos los datos normalmente
    usuarios = Cliente.objects.all()
    return render(request, 'MuestraDatos.html', {
        "clientes": usuarios,
        "perfil": perfil,
        "form": form,
        "mensaje": mensaje
    })


def buscar_cliente(email):
    try:
        return Cliente.objects.get(email=email)
    except Cliente.DoesNotExist:
        return None
        

def buscar_usuario(usuario,password):
    try:
        return Usuario.objects.get(usuario=usuario,password=password)
    except Usuario.DoesNotExist:
        return None

def borrar_cliente(request,id,perfil):
    cliente = Cliente.objects.get(id = id)
    cliente.delete()
    return redirect('DatosCliente',perfil = perfil)



