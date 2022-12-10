from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm 


def register(request):
	if request.method=='POST':
		register_form=RegisterForm(request.POST)
		if register_form.is_valid():
			register_form.save()
			messages.success(request,('New User Account Created'))
			return redirect('register')
	else:
		register_form=RegisterForm()
	return render(request,'account/register.html',{'register_form':register_form})