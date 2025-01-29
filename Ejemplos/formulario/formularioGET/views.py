from django.http import HttpResponse

from django.shortcuts import render

"""Version 1"""
def homeGET(request):
    return render(request,"home.html")
    
    

def saludo(request):
    nombre=request.GET['nombre']
    edad=int(request.GET['edad'])
    if (edad<18):
        mensaje=", Lo sentimos. No puedes acceder."
    else:
        mensaje=", Bienvenida"
    return render(request,'saludo.html',locals())


"""Versión 2, autollamada"""
"""def homeGET(request):
    if request.GET:
        nombre=request.GET['nombre']
        edad=int(request.GET['edad'])
        if (edad<18):
            mensaje=", Lo sentimos. No puedes acceder."
        else:
            mensaje=", Bienvenida"
       # return render(request,'saludo.html',locals())
        return render(request,'saludo.html',{'nombre':nombre,'mensaje':mensaje})
    else:
        return render(request,"home.html")
"""