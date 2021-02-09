from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
  first_name = forms.CharField(max_length=75, required=False)
  last_name = forms.CharField(max_length=75, required=False)
  email = forms.CharField(max_length=100, required=False)

  class Meta:
    model = User
    fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name',]

class CustomSignUpForm(UserCreationForm):
  
  class Meta:
    model = User
    fields = ['username','email', 'password1', 'password2',  'first_name', 'last_name',]
   
  