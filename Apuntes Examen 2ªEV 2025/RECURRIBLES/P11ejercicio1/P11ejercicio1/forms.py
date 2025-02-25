from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}),  # CORRECTO: Usamos TextInput como widget
        error_messages={'invalid': '* Introduce un usuario válido'}
    )

    #este error si no lo pones salta solo con uno en ingles
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

