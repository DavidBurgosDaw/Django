from django import forms
from gestion_incidencias.models import Incidencia, Laboratorio

class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=50, 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'invalid': '* Introduce un correo válido'}
    )
    password = forms.CharField(
        max_length=50, 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class AltaIncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ['laboratorio', 'numero_ordenador', 'descripcion']
        widgets = {
            'laboratorio': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'numero_ordenador': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'text-transform: uppercase;'}
            ),
            'descripcion': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
        }
