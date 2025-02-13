from django import forms

AFICIONES = [
    ('leer', 'Leer'),
    ('correr', 'Correr'),
    ('estudiar', 'Estudiar'),
    ('programar', 'Programar'),
    ('viajar', 'Viajar'),
]

class AficionesForm(forms.Form):
    nombre = forms.CharField(max_length=25, required=True, label="Nombre")
    aficiones = forms.MultipleChoiceField(
        choices=AFICIONES,
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Permite no seleccionar ninguna opción
        label="Aficiones"
    )

SEXO = [
    ("masculino","Masculino"),
    ("femenino","Femenino"),
    ("indefinido","Indefinido")
]

class UsuarioForm(forms.Form):
    nombre = forms.CharField( max_length=25, required=True, label="Nombre")
    apellidos = forms.CharField( max_length=25, required=True, label="Apellidos")
    edad = forms.IntegerField( required=True, label="Edad")
    sexo = forms.MultipleChoiceField( choices=SEXO, required=True, label="Sexo", widget=forms.CheckboxSelectMultiple)
    temas = forms.CharField(max_length=100,required=True,label="Temas")
    aficiones = forms.MultipleChoiceField(choices=AFICIONES, required=False, widget=forms.CheckboxSelectMultiple, label="Aficiones")
