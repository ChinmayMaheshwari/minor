from django.shortcuts import render
from .forms import SignUpForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def index(request):
	return render(request,'index.html')

def register(request):
	registered=False
	if request.method=='POST':
		user_form = SignUpForm(data=request.POST)

		if user_form.is_valid() and user_form.cleaned_data['password']==user_form.cleaned_data['confirm_password']:
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered=True
		else:
			if user_form.data['password'] != user_form.data['confirm_password']:
				user_form.add_error('password_confirm', 'The passwords do not match')
			print(user_form.errors)
	else:
		user_form=SignUpForm()

	return render(request,'register.html',{'user_form':user_form,'registered':registered})



def user_login(request):

	if request.method=='POST':
		username=request.POST.get("username")
		password=request.POST.get("password")

		user =authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('minor_project:index'))
			else:
				return HttpResponse("ACCOUNT Not ACTIVE")
		else:
			print("Someone tried to run login and failed!")
			print("Username : {} and password: {}".format(username,password))
			return HttpResponse("Invalid login try")
	else:
		return render(request,'login.html',{})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('minor_project:index'))
