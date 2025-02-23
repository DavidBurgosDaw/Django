# forms.py
from django import forms
from .models import Partido, Equipo

class PartidoForm(forms.ModelForm):
    #USANDO ModelForm para no tener que poner las validaciones otra vez como en el modelo
    class Meta:
        model = Partido
        fields = ['equipo_casa', 'goles_casa', 'equipo_visita', 'goles_visita']
        widgets = {
            'equipo_casa': forms.Select(attrs={'class': 'form-control'}),
            'goles_casa': forms.NumberInput(attrs={'class': 'form-control'}),
            'equipo_visita': forms.Select(attrs={'class': 'form-control'}),
            'goles_visita': forms.NumberInput(attrs={'class': 'form-control'})
        }
