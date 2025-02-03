from django.shortcuts import render
from datetime import datetime

def index(request):
    fecha_hora = datetime.now()
    return render(request,"index.html",{"fecha":fecha_hora})