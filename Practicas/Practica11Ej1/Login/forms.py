from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField( max_length=20, required=True)
    password = forms.CharField(max_length=20, required=True)