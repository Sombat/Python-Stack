from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
	return render(request,'index.html')

def register(request):
	errors = User.objects.register_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		# newUser = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
		hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		newUser = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hash1.decode())
		request.session['logged_in_user_id'] = newUser.id
	return redirect('/success')

def login(request):
	errors = User.objects.login_validator(request.POST)
	# print(request.session['email_2'])
	# print(request.POST['email'])
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		userinDB = User.objects.get(email=request.POST['email'])
		request.session['logged_in_user_id'] = userinDB.id
	return redirect('/success')

def success(request):
	if 'logged_in_user_id' in request.session:
		context = {
			'logged_in_user': User.objects.get(id=request.session['logged_in_user_id'])
		}
		return render(request, 'success.html', context)
	return redirect('/', context)

def logout(request):
	request.session.flush()
	return redirect('/')