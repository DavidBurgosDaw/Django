from django import forms
from .models import Laboratiorio

class loginForm(forms.Form):
    email = forms.EmailField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput()) #Lo pongo asi para que coja como charfield en vez de textfield

class AltaForm(forms.Form):
    laboratorio=forms.ChoiceField(choices=[(lab.nombre,lab.nombre) for lab in Laboratiorio.objects.all()],widget=forms.Select(attrs={'class':'form-control'}),label="Laboratorio")
    numPc=forms.CharField(max_length=10,required=True,widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Introduce tu nombre"}),label="Nº de Ordenador")
    descripcion = forms.CharField(widget=forms.Textarea)
