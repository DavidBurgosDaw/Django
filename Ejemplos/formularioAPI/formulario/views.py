from django.shortcuts import render
from formulario.forms import FormularioContacto
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    if request.POST:
        miFrm=FormularioContacto(request.POST)
        if miFrm.is_valid():
            dicc=miFrm.cleaned_data           
            return render(request, 'datos.html',dicc)
    else:
        miFrm=FormularioContacto()
    
    return render(request, "home.html",{"form":miFrm})
        
        
    