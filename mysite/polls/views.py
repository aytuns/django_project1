from django.shortcuts import render
from django.http import HttpResponse

def index(response):
	return HttpResponse("Hello, you are at poll's index")