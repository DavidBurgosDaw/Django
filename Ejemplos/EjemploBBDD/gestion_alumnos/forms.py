from django import forms


class FrmAlumno(forms.Form):
    nombre=forms.CharField(max_length=20,widget=forms.TextInput({'class':'form-control','placeholder':"Tu nombre"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'ejemplo@ejemplo.com'}))
    dni=forms.CharField(max_length=9,widget=forms.TextInput({'class':'form-control','placeholder':"Tu DNI"}),)
    nota=forms.DecimalField(max_digits=4,decimal_places=2,widget=forms.TextInput({'class':'form-control','placeholder':"Tu nota"}))

class FrmbuscarAlumno(forms.Form):
    dni=forms.CharField(max_length=9,widget=forms.TextInput({'class':'form-control','placeholder':"Tu DNI"}),)
    
