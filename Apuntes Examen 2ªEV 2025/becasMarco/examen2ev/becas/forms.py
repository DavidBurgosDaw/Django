from django import forms
from becas.models import Solicitud, Usuario

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['dni', 'provincia', 'renta', 'edad']

        # Personalizar widgets (apariencia de los campos)
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su dni'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su provincia'}),
            'renta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su renta'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la edad'}),
        }


class ConsultaForm (forms.Form):
     dni = forms.CharField(max_length=9, label="dni", 
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su dni'}))
     
class LoginForm (forms.Form):
    usuario = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Usuario:"})
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Contraseña:"})
    )
