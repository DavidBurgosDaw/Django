from django.shortcuts import render

def home(request):
    mensaje = "Hola, mi primer ejemplo con plantillas en DJANGO"
    return render(request,"welcome.html", {'mensaje': mensaje})