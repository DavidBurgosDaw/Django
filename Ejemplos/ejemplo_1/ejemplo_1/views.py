from django.shortcuts import render
from models.persona import Persona  # Asegúrate de que la ruta de importación sea correcta

def saluda(request):
    # Crear una instancia de la clase Persona
    p = Persona('Rosa', 34)
    
    # Contexto para pasar a la plantilla
    contexto = {
        'nombre': "Rosa",
        'mensaje': ", estoy saludando a la clase: HOLA DAW2!!!!!!",
        'l': [6, 7, 3, 4],  # Lista de ejemplo para mostrar en la plantilla
        'person': p  # Objeto Persona
    }
    
    # Renderizar la plantilla 'index.html' con el contexto
    return render(request, 'index.html', contexto)

def despedida(request):
    # Renderizar la plantilla 'salir.html'
    return render(request, 'salir.html')
