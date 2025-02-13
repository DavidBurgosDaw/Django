from django.shortcuts import render
from .forms import AficionesForm, UsuarioForm

def infoUsuario(request):
    if request.method == "POST":
        form = AficionesForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            aficiones = form.cleaned_data["aficiones"]
            return render(request,"infoUsuarioRes.html", {"nombre":nombre,"aficiones":aficiones})
    else:
        form = AficionesForm()

    return render(request,"infoUsuario.html",{"form":form})

def usuarioForm(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellidos = form.cleaned_data["apellidos"]
            edad = form.cleaned_data["edad"]
            sexo = form.cleaned_data["sexo"]
            temas = form.cleaned_data["temas"]
            aficiones = form.cleaned_data["aficiones"]
            return render(request,"usuarioRes.html", {"nombre":nombre,"apellidos":apellidos,"edad":edad,"sexo":sexo,"temas":temas,"aficiones":aficiones})
    else:
       
        form = UsuarioForm()

    return render(request,"usuario.html",{"form":form})