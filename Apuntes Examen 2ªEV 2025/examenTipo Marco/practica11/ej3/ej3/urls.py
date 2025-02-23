from django.urls import path
from gestion_clientes import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('lista_usuarios/', views.lista_clientes_normal, name='lista_usuarios'),
    path('admin_usuarios/', views.lista_clientes_admin, name='admin_usuarios'),
    path('eliminar_cliente/<str:nombre>/', views.eliminar_cliente, name='eliminar_cliente'),
]
