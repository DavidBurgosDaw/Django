from django import forms
from django.core.validators import RegexValidator 

class BecasFP(forms.Form):
    DNI = forms.CharField(
        max_length=9,  # DNI tiene 8 números + 1 letra
        min_length=9,  # Asegura que tenga exactamente 9 caracteres
        validators=[RegexValidator(
                regex=r'^[0-9]{8}[A-Z]$',
                message='Formato de DNI inválido. Debe ser 8 números seguidos de una letra mayúscula (ejemplo: 12345678A)'
            )
        ],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Introduce tu DNI (12345678A)',
                'pattern': '[0-9]{8}[A-Z]',  # Validación HTML5
                'title': '8 números seguidos de una letra mayúscula'
            }
        )
    ) 
    provinvia=forms.CharField(widget=forms.CharField(attrs={'class':'form-control','placeholder':'provincia'}))
    rentPerCapita=forms.IntegerField(max_length=max,widget=forms.IntegerField({'class':'form-control','placeholder':"renta per capita"}),)
    nota=forms.DecimalField(max_digits=4,decimal_places=2,widget=forms.TextInput({'class':'form-control','placeholder':"Tu nota"}))


class Usuario(forms.Form):
    username = forms.CharField(max_length=50, unique=True)
    password = forms.CharField(max_length=50)  