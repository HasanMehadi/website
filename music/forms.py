from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'password']
