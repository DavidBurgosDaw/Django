

from django.http import HttpResponse
from django.shortcuts import render



def saluda(request):
    #return HttpResponse("HOLA DAW2!!!!");
    p=Persona('Rosa',34)
    contexto={'nombre':"Rosa",
              'mensaje':", estoy salundado a la clase: HOLA DAW2!!!!!!",  
              'l': [6,7,3,4],     
              'person':p       
              }
    return render(request, 'index.html',contexto)
    return render(request,'index.html');

def despedida(request):
    return render(request,'salir.html')