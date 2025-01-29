from django.shortcuts import  render


def home(request):
    return render(request,'home_template.html')
   


def saludo(request):
    nombre=request.POST['nombre']
    edad=int(request.POST['edad'])
    if (nombre and edad):
        if (edad<60):
            mensaje="Jovencit@!!!!"
        else:
            mensaje="Ya no eres tan jovencit@......"
    else:
        mensaje="Introduce los datos pedidos"
    return render(request,'saludo_template.html', {"nombre":nombre,"mensaje":mensaje}  ) 
   