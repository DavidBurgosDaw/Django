from django.shortcuts import render, redirect, get_object_or_404
from gestion_clientes.forms import LoginForm, ClienteForm
from gestion_clientes.models import Usuario, Cliente

def Login(request):
    mensaje = ""

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            password = form.cleaned_data['password']
            usuario = buscar_usuario(nickname)

            if usuario is None:
                mensaje = "Usuario no encontrado"
            elif usuario.password != password:  
                mensaje = "Contraseña incorrecta"
            else:
                if usuario.perfil == "normal":
                    return redirect('lista_usuarios')
                else:
                    return redirect('admin_usuarios')

    else:
        form = LoginForm()

    return render(request, 'gestion_clientes/login.html', {'form': form, 'mensaje': mensaje})

def buscar_usuario(nickname):
    try:
        return Usuario.objects.get(nickname=nickname)
    except Usuario.DoesNotExist:
        return None

def lista_clientes_normal(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion_clientes/lista_clientes.html', {'lista_clientes': clientes})

def lista_clientes_admin(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_usuarios')
    else:
        form = ClienteForm()

    clientes = Cliente.objects.all()
    return render(request, 'gestion_clientes/lista_clientes_admin.html', {'lista_clientes': clientes, 'form': form})

def eliminar_cliente(request, nombre):
    cliente = Cliente.objects.get(nombre=nombre) #seleccionar cliente
    cliente.delete() #eliminar cliente
    return redirect('admin_usuarios')
