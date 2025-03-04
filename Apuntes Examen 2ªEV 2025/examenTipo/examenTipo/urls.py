"""
URL configuration for examenTipo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from gestion_incidencias import views #Importo las vistas de gestion_incidencias

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Login, name='login'),
    path('profesor/<str:email>/', views.Profesor_View, name='profesor'),
    path('tecnico/<str:email>/', views.Tecnico_View, name='tecnico'),
    path('tecnico/<str:email>/', views.Tecnico_View, name='tecnico'),
    path('resolver_incidencia/<int:numero>/', views.resolver_incidencia, name='resolver_incidencia'),
    path('detalles_incidencia/<int:numero>/', views.detalles_incidencia, name='detalles_incidencia'),
]
