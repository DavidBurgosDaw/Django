from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField( max_length=20, required=True)
    password = forms.CharField(max_length=20, required=True)

class RegisterForm(forms.Form):
    usuario = forms.CharField( max_length=20, required=True)
    password = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=100,required=True)
    ciudad = forms.CharField(max_length=30)