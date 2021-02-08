from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Userreg(UserCreationForm):
	password1=forms.CharField(widget=(forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'})))
	password2=forms.CharField(widget=(forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter confirm password'})))
	class Meta:
		model = User
		fields = ['username','email']
		widgets={
		'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}),
		'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
		}
