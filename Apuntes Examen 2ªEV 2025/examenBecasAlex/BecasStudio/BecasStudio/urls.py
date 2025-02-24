from django.contrib import admin
from django.urls import path, include  # Importa include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion_becas.urls')),  
]