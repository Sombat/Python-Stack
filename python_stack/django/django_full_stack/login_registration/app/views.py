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
		hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		newUser = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hash1.decode())
		request.session['logged_in_user_id'] = newUser.id
	return redirect('/success')

def login(request):
	errors = User.objects.login_validator(request.POST)
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

def wall(request): # Definition for display messages and comments on wall.
	context = {
		"all_messages": Message.objects.all().order_by('-created_at'), # Passes all "Message" (see models.py for class) objects as context to wall (sorted by created_at date in descending order), so that it can be available for the template to display
		"all_comments": Comment.objects.all().order_by('-created_at'), # Passes all "Comment" objects (see models.py for class) as context to wall (sorted by created_at date in descending order), so that it can be available for the template to display
	}
	return render(request,'wall.html', context)

def post_message(request): # Definition for POST action url for message form.
	logged_in_user = User.objects.get(id=request.session['logged_in_user_id']) # Creates a variable called logged_in_user, that is set to the User that is currently logged in. The currently logged in User is set by taking the User ID from the session variable "logged_in_user_id", which is set when a User registers or logs in, and is clared when they log out.
	newMessage = Message.objects.create(message=request.POST['wall-message'], user=logged_in_user) # Creates a new "Message" by taking the message from the "wall-message" field on the message form at the top of wall.html, as well as setting the "user" ForeignKey (line 46 in models.py) to "logged_in_user", the variable that was created in the line above.
	return redirect('/wall')

def post_comment(request): # Definition for POST action url for comment form.
	logged_in_user = User.objects.get(id=request.session['logged_in_user_id']) # Creates a variable called "logged_in_user", that is set to the User that is currently logged in. The currently logged in User is set by taking the User ID from the session variable "logged_in_user_id", which is set when a User registers or logs in, and is clared when they log out.
	message_to_comment_on = Message.objects.get(id=request.POST['message_to_comment_on_id']) # Creates a variable called "message_to_comment_on", that is set to the message that the comment needs to be tied to by getting that message's ID from the "message_to_comment_on_id" field on the comment form in wall.html.
	newComment = Comment.objects.create(comment=request.POST['wall-comment'], user=logged_in_user, message=message_to_comment_on) # Creates a new "Comment" by taking the content from the "wall-comment" field on the comment form, and setting the user and message (lined 52 and 53 on models.py) to the variables "logged_in_user" and "message_to_comment_on", which we created in the lines above.
	return redirect('/wall')