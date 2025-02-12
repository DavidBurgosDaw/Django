from django.shortcuts import render
from Practica9Ej4.Models.Lenguaje import Plantilla
def index(request):
    x = [
        Plantilla(nombre = "Java", año = 2000, descripcion = "Lenguaje de programacion orientado a objetos procedente de C"),
        Plantilla(nombre = "C#", año = 1999, descripcion = "Lenguaje de programacion orientado a objetos procedente de C"),
        Plantilla(nombre = "JavaScript", año = 2005, descripcion = "Lenguaje de programacion orientado a web"),
        Plantilla(nombre = "Python", año = 2010, descripcion = "Lenguaje de programacion no orientado a objetos, muy bueno para inteligencias artificiales" )
    ]

          
  
    return render(request,"lenguajes.html",  {"plantillas" : x})