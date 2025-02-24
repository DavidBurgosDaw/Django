from django import forms
from app.models import *


class FrmLogin(forms.Form):
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={'invalid': '* Introduce un correo válido'}) 
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class FrmIncidencia(forms.ModelForm):
    laboratorio = forms.ModelChoiceField(
        queryset=Laboratorio.objects.all(),
        empty_label="Selecciona un laboratorio",
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    numero_ordenador = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: PC00'}),
        label="Número de ordenador",
        required=True,
        help_text="Introduce el identificador del ordenador afectado."
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe brevemente el problema'}),
        label="Descripción del problema",
        required=True
    )
    class Meta:
        model = Incidencia
        fields = ['laboratorio', 'numero_ordenador', 'descripcion']
        
class FrmGestionarIncidencia(forms.Form):
   # numero = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 1'}),label="Número de Incidencia",required=True,help_text="Introduce el ID")
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe brevemente el problema'}),
        label="Descripción del problema",
        required=True
    )