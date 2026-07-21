from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):
    # compulsary class meta inside 
    class Meta:
        model = Tweet
        fields = ['text' , 'photo']
        
class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model = User
        # here we are passing tuple because we're using built in form/ table
        fields= ('username', 'email', 'password1', 'password2')