from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	confirm_password=forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User 
		fields = ('username','first_name','last_name','email','password','confirm_password')


		