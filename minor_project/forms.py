from django import forms
from django.contrib.auth.models import User
from .models import ModelFormWithFile

class SignUpForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	confirm_password=forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User 
		fields = ('username','first_name','last_name','email','password','confirm_password')


class UploadFileForm(forms.ModelForm):
    #file = forms.FileField()
    class Meta():
   		model = ModelFormWithFile
   		fields = ('name','upload')
