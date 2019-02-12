from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nazwa użytkownika", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Hasło", max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control'}))
