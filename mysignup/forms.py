from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class SignupForm(UserCreationForm):
    password2=forms.CharField(label='Confirm password(again)',widget=forms.PasswordInput)
    class Meta:
        model=User
        #change the sequence of fiellds using "fields"
        fields=['username','first_name','last_name','email']
        #change the labele of predefine models using "labels"
        #labels={"email":"Email-id"}

class EditUserProfile(UserChangeForm):
    password=None
    class Meta:
        model=User 
        fields=['username','first_name','last_name','email']
        labels={'email':'Email-id'}