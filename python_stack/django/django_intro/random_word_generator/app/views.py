from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
	if 'counter' not in request.session:
		request.session['counter'] = 1
	return render(request, "index.html")

def random(request):
	request.session['generated_word'] = get_random_string(length=14)
	request.session['counter'] = request.session['counter'] + 1
	return redirect('/')

def reset(request):
	request.session.clear()
	request.session['generated_word'] = get_random_string(length=14)
	return redirect('/')