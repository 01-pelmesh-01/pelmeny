from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm , TextInput , EmailInput , FileInput , ModelForm

from .models import CustomUser , story

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class story_f(ModelForm):
    class Meta:
        model = story
        fields = ['name','desс' , 'image']

        widgets = {
            "name ": TextInput (attrs = { 'placeholder': 'THEM'}),
            "desс" : TextInput (attrs = { 'placeholder': 'MAIN'}),
            "image" : FileInput (attrs = { 'placeholder': 'VISUAL'}),
            }

