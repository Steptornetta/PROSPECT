
# Create your views here.
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from .forms import NameForm
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')
	
		


