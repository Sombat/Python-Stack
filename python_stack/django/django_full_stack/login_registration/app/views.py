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

def wall(request):
	context = {
		"all_messages": Message.objects.all().order_by('-created_at'),
		"all_comments": Comment.objects.all().order_by('-created_at'),
	}
	# print(Comment.objects.all())
	return render(request,'wall.html', context)

def post_message(request):
	logged_in_user = User.objects.get(id=request.session['logged_in_user_id'])
	newMessage = Message.objects.create(message=request.POST['wall-message'], user=logged_in_user)
	return redirect('/wall')

def post_comment(request):
	logged_in_user = User.objects.get(id=request.session['logged_in_user_id'])
	message_to_comment_on = Message.objects.get(id=request.POST['message_to_comment_on_id'])
	# print(message_to_comment_on)
	# print(logged_in_user.last_name)
	# print(request.POST['wall-comment'])
	# need to get id and attach comments to right message, also add to template
	newComment = Comment.objects.create(comment=request.POST['wall-comment'], user=logged_in_user, message=message_to_comment_on)
	return redirect('/wall')