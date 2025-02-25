from django.urls import path
from . import views  # ✅ Importa las vistas de TU APLICACIÓN

app_name = 'gestion_becas'

urlpatterns = [
    path('', views.index, name='index'),
    
]