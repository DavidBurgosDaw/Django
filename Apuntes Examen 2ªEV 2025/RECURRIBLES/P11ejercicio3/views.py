from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
                nombre=form.cleaned_data['nombre']
                ciudad=form.cleaned_data['ciudad']
                telefono=form.cleaned_data['telefono']
                email=form.cleaned_data['email']
                print(nombre)
                cliente = Cliente(nombre=nombre, ciudad=ciudad, telefono=telefono, email=email)
                print(cliente.nombre)
                cliente.save()
                clientes = Cliente.objects.all() 
                form = ClienteForm()  
                return render(request, 'Admin.html', {'clientes': clientes,  'form': form})
    else:
        
        lista_clientes = Cliente.objects.all()
        form = ClienteForm()  
    
    return render(request, 'Admin.html', {'clientes': lista_clientes, 'form': form})

def lista_clientes(request):
    clientes = Cliente.objects.all() 
    return render(request, 'Admin.html', {'clientes': clientes})