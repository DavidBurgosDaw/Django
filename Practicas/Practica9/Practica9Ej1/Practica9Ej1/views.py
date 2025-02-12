from django.shortcuts import render

def edadFutura(request, edadActual, anio_futuro):
    # Calcula la edad futura
    edad_futura = edadActual + (anio_futuro - 2025)
    
    # Retorna el resultado a la plantilla
    return render(request, 'index.html', {'edad_futura': edad_futura, 'anio_futuro': anio_futuro})
