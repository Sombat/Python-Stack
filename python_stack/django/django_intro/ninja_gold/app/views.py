from django.shortcuts import render, redirect
import random, datetime

def index(request):
	if 'gold' in request.session:
		print(f"Ninja has {request.session['gold']}.")
	else:
		request.session['gold'] = 0
		request.session['activity'] = ''
		print(f"Ninja just walked in the door.")
	return render(request,'index.html')

def chaching(request):
	if request.POST['building'] == 'farm':
		tempNumber = random.randint(10, 20)
		if random.randint(1, 2) < 2:
			request.session['gold'] = request.session['gold'] - tempNumber
			print(f"Entered a farm and lost {tempNumber} golds... Ouch.")
			request.session['activity'] = request.session['activity'] + f"<p class='lost'>Entered a farm and lost {tempNumber} golds... Ouch.</p>" + "\n"
		else:
			request.session['gold'] = request.session['gold'] + tempNumber
			print(f"Earned {tempNumber} golds from farm!")
			request.session['activity'] = request.session['activity'] + f"<p class='win'>Earned {tempNumber} golds from farm!</p>" + "\n"
		print(request.session['activity'])
	elif request.POST['building'] == 'cave':
		tempNumber = random.randint(5, 10)
		if random.randint(1, 2) < 2:
			request.session['gold'] = request.session['gold'] - tempNumber
			print(f"Entered a cave and lost {tempNumber} golds... Ouch.")
			request.session['activity'] = request.session['activity'] + f"<p class='lost'>Entered a cave and lost {tempNumber} golds... Ouch.</p>" + "\n"
		else:
			request.session['gold'] = request.session['gold'] + tempNumber
			print(f"Earned {tempNumber} golds from cave!")
			request.session['activity'] = request.session['activity'] + f"<p class='win'>Earned {tempNumber} golds from cave!</p>" + "\n"
		print(request.session['activity'])
	elif request.POST['building'] == 'house':
		tempNumber = random.randint(2, 5)
		if random.randint(1, 2) < 2:
			request.session['gold'] = request.session['gold'] - tempNumber
			print(f"Entered a house and lost {tempNumber} golds... Ouch.")
			request.session['activity'] = request.session['activity'] + f"<p class='lost'>Entered a house and lost {tempNumber} golds... Ouch.</p>" + "\n"
		else:
			request.session['gold'] = request.session['gold'] + tempNumber
			print(f"Earned {tempNumber} golds from house!")
			request.session['activity'] = request.session['activity'] + f"<p class='win'>Earned {tempNumber} golds from house!</p>" + "\n"
		print(request.session['activity'])
	elif request.POST['building'] == 'casino':
		tempNumber = random.randint(0, 50)
		if random.randint(1, 2) < 2:
			request.session['gold'] = request.session['gold'] - tempNumber
			print(f"Entered a casino and lost {tempNumber} golds... Ouch.")
			request.session['activity'] = request.session['activity'] + f"<p class='lost'>Entered a casino and lost {tempNumber} golds... Ouch.</p>" + "\n"
		else:
			request.session['gold'] = request.session['gold'] + tempNumber
			print(f"Earned {tempNumber} golds from casino!")
			request.session['activity'] = request.session['activity'] + f"<p class='win'>Earned {tempNumber} golds from casino!</p>" + "\n"
		print(request.session['activity'])
	return redirect('/')

def destroy(request):
    request.session.clear()
    print('User liked the game so much, they decided to play again!')
    return redirect('/')