from django import forms
from django.core.validators import EmailValidator
from .models import Incidencia


class FrmLogin(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@ejemplo.com'}),
        validators=[EmailValidator(message="Ingrese un email válido")],  # ✅ Corregido aquí
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'})
    )

class IncidenciaForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )

    laboratorio_choices = [
        ('Lab1', 'Lab1'),
        ('Lab2', 'Lab2'),
        ('Lab3', 'Lab3'),
        ('Lab4', 'Lab4'),
        ('Lab5', 'Lab5'),
    ]

    laboratorio = forms.ChoiceField(
    choices=laboratorio_choices,
    widget=forms.Select(attrs={'class': 'form-control'}),
    required=True,
    label="Laboratorio"
    )


    numero_ordenador = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}), #aqui metes los placeholders
    )

class ResolverIncidenciaForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        label="Email del Técnico"
    )

    numero_incidencia = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        label="Número de Incidencia"
    )

    descripcion_resolucion = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Describe cómo se resolvió la incidencia...',
            'rows': 4
        }),
        label="Descripción de la Resolución"
    )

class DetallesForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control',"readonly":"readonly"}),
    )


    laboratorio = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control',"readonly":"readonly"}),

    ) 


    numero_ordenador = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',"readonly":"readonly"}),
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control',"readonly":"readonly"}), #aqui metes los placeholders
    )