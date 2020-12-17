from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    roll_number = forms.CharField(max_length = 9)
    room_number = forms.IntegerField()
    interests = forms.CharField(max_length = 100)

    class Meta:
        model = User
        fields = ['username', 'email', 'roll_number','room_number','interests','password1', 'password2']