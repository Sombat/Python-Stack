from __future__ import unicode_literals
from django.db import models
import re, bcrypt

class UserManager(models.Manager):
	def register_validator(self, postData):
		errors = {}
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if len(postData['first_name']) < 2 or str.isalpha(postData['first_name']) == False:
			errors["first_name"] = "First name should be at least 2 characters, and contain only letters."
		if len(postData['last_name']) < 2 or str.isalpha(postData['last_name']) == False:
			errors["last_name"] = "Last name should be at least 2 characters, and contain only letters."
		if not EMAIL_REGEX.match(postData['email']):       
			errors['email'] = "Invalid email address."
		if len(postData['password']) < 8:
			errors["last_name"] = "Password should be at least 8 characters, and contain only letters."
		if postData['password'] != postData['confirm_password']:
			errors["password"] = "Password and confirmation does not match."
		return errors

	def login_validator(self, postData):
		userinDB_filter = User.objects.filter(email=postData['email'])
		print(userinDB_filter)
		# print(postData['email'])
		errors = {}
		if len(userinDB_filter) == 0:
			errors['email'] = "User does not exist."
		else:
			userinDB_get = User.objects.get(email=postData['email'])
			if not bcrypt.checkpw(postData['password'].encode(), userinDB_get.password.encode()):
			# if postData['password'] != userinDB_get.password:       
				errors['password'] = "Password does not match."
		print(errors)
		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Message(models.Model):
	user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	message = models.TextField()

class Comment(models.Model):
	user = models.ForeignKey(User, related_name="comments_user", on_delete=models.CASCADE)
	message = models.ForeignKey(Message, related_name="comments_message", on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	comment = models.TextField()