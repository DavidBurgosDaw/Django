from django import forms
from gestion_inc.models import Incidencia, Laboratorio

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={'invalid': '* Introduce un correo válido'}) 
    #este error si no lo pones salta solo con uno en ingles
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
class AltaIncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ['laboratorio', 'numero_ordenador', 'descripcion']

        # Personalizar widgets (apariencia de los campos)
        laboratorio = forms.ModelChoiceField(
            queryset=Laboratorio.objects.all(),
            empty_label="Selecciona un laboratorio",
            widget=forms.Select(attrs={'class': 'form-control'})
        )
        numero_ordenador = forms.CharField(
            max_length=50, 
            widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'text-transform: uppercase;'})
        )
        descripcion = forms.CharField(
            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        )
