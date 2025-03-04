"""
URL configuration for EjercicioAlbertoBBDD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Primera.views import Log, EditAl, AñadirAl, añadirTar, cambiarEstado, eliminar

urlpatterns = [
    path('', Log, name="log"),
    path('editar/<str:id>', EditAl, name="ed"),
    path('añadir/<str:id>', AñadirAl, name="añ"),
    path('añadirTar/<str:id>', añadirTar, name="tar"),
    path('entregar/<str:id>', cambiarEstado, name="en"),
    path('eliminar/<str:id>', eliminar, name="el"),

]
