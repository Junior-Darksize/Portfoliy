from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username','password1','password2']



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()