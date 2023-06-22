from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	#return HttpResponse("Hello, you are at poll's index page")
	return render(request, 'index.html')
