
# Create your views here.
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

def home(request):
	return HttpResponse("Home Page")

def hello(request):
    return HttpResponse("Hello world") 

def index(request):
    return render(request, 'index.html')
	
def myworld(request):
	return render(request, 'myworld.html')
	
	