from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Usuario

# Create your views here.
def login(request):
    if request.POST:
        miFrm = LoginForm(request.POST)
        if miFrm.is_valid():
            username = miFrm.cleaned_data['username']
            return redirect('edit.html', username=username)  # Asegúrate de tener una URL nombrada 'edit'
    else:
        miFrm = LoginForm()
    return render(request, "login.html", {"form": miFrm})


    
def edit(request, username):
    try:
        usuario = Usuario.objects.get(username=username)
        return render(request,'edit.html', {'usuario': usuario})
    except Usuario.DoesNotExist:
        miFrm = LoginForm()
        return render(request,"login.html",{"form": miFrm})
    
   