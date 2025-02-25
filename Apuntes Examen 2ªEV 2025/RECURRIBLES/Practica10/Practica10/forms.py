from django import forms
from django.core.validators import EmailValidator

class FormularioContacto(forms.Form):
    nombre = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Tu nombre"
        }),
        label="Nombre"
    )
    
    email = forms.EmailField(
        required=True,
        validators=[EmailValidator(message="Ingresa un email válido")],
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com'
        }),
        error_messages={
            'required': 'El email es obligatorio',
            'invalid': 'Por favor ingresa un email válido'
        }
    )    
    
    SEXO = [
        ('mujer', 'Femenino'),
        ('hombre', 'Masculino')
    ]
    
    TEMAS = [
        ('progra', 'Programación'),
        ('asir', 'Asir')
    ]
    
    AFICIONES = [
        ('viajar', 'Viajar'),
        ('beber', 'Beber')
    ]
    
    sexo = forms.ChoiceField(
        choices=SEXO, 
        widget=forms.RadioSelect
    )
    
    temas = forms.ChoiceField(
        choices=TEMAS, 
        widget=forms.Select
    )    
    
    aficiones = forms.MultipleChoiceField(
         required=False,
        choices=AFICIONES, 
        widget=forms.CheckboxSelectMultiple
    )

    autorizacion = forms.BooleanField(
        required=False, 
        label="Autorizo el tratamiento de mis datos"
    )