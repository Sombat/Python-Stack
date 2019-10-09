from django.shortcuts import render
from time import gmtime, strftime

def index(request):
	context = {
		"time": strftime("%Y-%m-%d %H:%M %p", gmtime())
	}
	print(context)
	return render(request,'time_display_app/index.html', context)