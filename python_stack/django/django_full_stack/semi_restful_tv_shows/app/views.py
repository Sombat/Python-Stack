from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

def index(request):
	return redirect('/shows')

def all_shows(request):
	context = {
		"all_shows": Show.objects.all()
	}
	return render(request,'index.html', context)

def new_show(request):
	return render(request,'new_show.html')

def create_show(request):
	errors = Show.objects.basic_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/shows/new')
	else:
		tempShow = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['desc'])
		messages.success(request, "Show successfully added.")
		return redirect('/shows/' + str(tempShow.id))

def show_details(request,id):
	context = {
		"this_show": Show.objects.get(id=id),
	}
	# if request.method == "POST":
	# 	author_id = request.POST['author_id']
	# 	author_to_add = Author.objects.get(id=author_id)
	# 	book_to_add = Book.objects.get(id=id)
	# 	author_to_add.books.add(book_to_add)
	# context = {
	# 	"book": Book.objects.get(id=id),
	# 	"all_book_authors": Author.objects.all(),
	# 	"current_id": id
	# }
	return render(request,'show_detail.html', context)

def edit_show(request,id):
	context = {
		"this_show": Show.objects.get(id=id),
	}
	return render(request,'edit_show.html', context)

def update_show(request,id):
	errors = Show.objects.basic_validator(request.POST)
	tempShow = Show.objects.get(id=id)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/shows/' + str(tempShow.id) + '/edit')
	else:
		if tempShow.title != request.POST['title']:
			tempShow.title = request.POST['title']
		if tempShow.network != request.POST['network']:
			tempShow.network = request.POST['network']
		if tempShow.release_date != request.POST['release_date']:
			tempShow.release_date = request.POST['release_date']
		if tempShow.desc != request.POST['desc']:
			tempShow.desc = request.POST['desc']
		tempShow.save()
	return redirect('/shows/' + str(tempShow.id))

def delete_show(request,id):
	tempShow = Show.objects.get(id=id)
	tempShow.delete()
	return redirect('/shows')