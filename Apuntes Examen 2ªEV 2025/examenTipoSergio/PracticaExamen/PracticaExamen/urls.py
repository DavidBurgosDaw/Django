"""
URL configuration for PracticaExamen project.

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
from os import name
from depart_informatica.views import login,profesor_view,profesor_incidencia,tecnico_view,resolver,detalles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login,name='login'),
    path('profesor/<str:email>/', profesor_view, name='profesor_view'),  # ✅ Ruta para la vista profesor
    path('profesor_incidencia/<str:email>/', profesor_incidencia, name='profesor_incidencia'),  # ✅ Ruta para la vista profesor
    path('tecnico/<str:email>/',tecnico_view,name="tecnico_view"),
    path('resolver/<str:email>/<int:numero_incidencia>',resolver,name="resolver"),
    path('detalles/<int:numero_incidencia>',detalles,name="detalles")
    
]

