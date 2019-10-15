from django.shortcuts import render, redirect, HttpResponse
from .models import *

def index(request):
	context = {
		"all_books": Book.objects.all()
	}
	return render(request,'index.html', context)

def add_book(request):
	Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
	return redirect('/')

def books(request):
	return redirect('/')

def book_details(request,id):
	if request.method == "POST":
		author_id = request.POST['author_id']
		author_to_add = Author.objects.get(id=author_id)
		book_to_add = Book.objects.get(id=id)
		author_to_add.books.add(book_to_add)
	context = {
		"book": Book.objects.get(id=id),
		"all_book_authors": Author.objects.all(),
		"current_id": id
	}
	return render(request,'book_detail.html', context)

# def add_author_to_book(request,id):
# 	author_id = request.POST['author_id']
# 	author_to_add = Author.objects.get(id=author_id)
# 	book_to_add = Book.objects.get(id=id)
# 	author_to_add.books.add(book_to_add)
# 	context = {
# 		"book": Book.objects.get(id=id),
# 		"all_book_authors": Author.objects.all(),
# 		"current_id": id
# 	}
# 	return redirect(request.path_info, context)

def authors(request):
	context = {
		"all_authors": Author.objects.all()
	}
	return render(request,'authors.html', context)

def author_details(request,id):
	if request.method == "POST":
		book_id = request.POST['book_id']
		book_to_add = Book.objects.get(id=book_id)
		author_to_add = Author.objects.get(id=id)
		book_to_add.authors.add(author_to_add)
	context = {
		"author": Author.objects.get(id=id),
		"all_author_books": Book.objects.all(),
		"current_id": id
	}
	return render(request,'author_detail.html', context)

def add_author(request):
	Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
	return redirect('/authors')

# def chaching(request):
# 	if request.POST['building'] == 'farm':
# 		tempNumber = random.randint(10, 20)
# 		if random.randint(1, 2) < 2:
# 			request.session['gold'] = request.session['gold'] - tempNumber
# 			print(f"Entered a farm and lost {tempNumber} golds... Ouch.")
# 			request.session['activity'] = request.session['activity'] + f"<p class='lost'>Entered a farm and lost {tempNumber} golds... Ouch.</p>" + "\n"
# 		else:
# 			request.session['gold'] = request.session['gold'] + tempNumber
# 			print(f"Earned {tempNumber} golds from farm!")
# 			request.session['activity'] = request.session['activity'] + f"<p class='win'>Earned {tempNumber} golds from farm!</p>" + "\n"
# 		print(request.session['activity'])
# 	elif request.POST['building'] == 'cave':
# 		tempNumber = random.randint(5, 10)
# 		if random.randint(1, 2) < 2:
# 			request.session['gold'] = request.session['gold'] - tempNumber
# 			print(f"Entered a cave and lost {tempNumber} golds... Ouch.")
# 			request.session['activity'] = request.session['activity'] + f"<p class='lost'>Entered a cave and lost {tempNumber} golds... Ouch.</p>" + "\n"
# 		else:
# 			request.session['gold'] = request.session['gold'] + tempNumber
# 			print(f"Earned {tempNumber} golds from cave!")
# 			request.session['activity'] = request.session['activity'] + f"<p class='win'>Earned {tempNumber} golds from cave!</p>" + "\n"
# 		print(request.session['activity'])
# 	elif request.POST['building'] == 'house':
# 		tempNumber = random.randint(2, 5)
# 		if random.randint(1, 2) < 2:
# 			request.session['gold'] = request.session['gold'] - tempNumber
# 			print(f"Entered a house and lost {tempNumber} golds... Ouch.")
# 			request.session['activity'] = request.session['activity'] + f"<p class='lost'>Entered a house and lost {tempNumber} golds... Ouch.</p>" + "\n"
# 		else:
# 			request.session['gold'] = request.session['gold'] + tempNumber
# 			print(f"Earned {tempNumber} golds from house!")
# 			request.session['activity'] = request.session['activity'] + f"<p class='win'>Earned {tempNumber} golds from house!</p>" + "\n"
# 		print(request.session['activity'])
# 	elif request.POST['building'] == 'casino':
# 		tempNumber = random.randint(0, 50)
# 		if random.randint(1, 2) < 2:
# 			request.session['gold'] = request.session['gold'] - tempNumber
# 			print(f"Entered a casino and lost {tempNumber} golds... Ouch.")
# 			request.session['activity'] = request.session['activity'] + f"<p class='lost'>Entered a casino and lost {tempNumber} golds... Ouch.</p>" + "\n"
# 		else:
# 			request.session['gold'] = request.session['gold'] + tempNumber
# 			print(f"Earned {tempNumber} golds from casino!")
# 			request.session['activity'] = request.session['activity'] + f"<p class='win'>Earned {tempNumber} golds from casino!</p>" + "\n"
# 		print(request.session['activity'])
# 	return redirect('/')

# def destroy(request):
#     request.session.clear()
#     print('User liked the game so much, they decided to play again!')
#     return redirect('/')