"""EjemploBBDD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from gestion_alumnos.views import eliminar, home,anyadir,buscar,modificar,listado,listado_aprobados,detalle_alumno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('addAlum',anyadir,name="add"),
    path('deleteAlum',eliminar,name='delete'),
    path('searchAlum',buscar,name='search'),
    path('updateAlum',modificar,name="update"),
    path('listAlums',listado,name='listall'),
    path('listAprobados',listado_aprobados,name='listApto'),
    path('showAlumn/<int:numero>', detalle_alumno,name="detalle")
]
