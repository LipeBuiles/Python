from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Personas

class RegistroForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True, help_text='Requerido. 50 caracteres como máximo y con el cual realizaras login.')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ["is_staff", 'username', 'first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["is_staff", 'username', 'first_name', 'last_name', 'email', "is_staff"]