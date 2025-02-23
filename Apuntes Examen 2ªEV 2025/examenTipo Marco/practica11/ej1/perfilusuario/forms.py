from django import forms

class FrmLogin(forms.Form):
    nickname = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Usuario:"})
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Contraseña:"})
    )
