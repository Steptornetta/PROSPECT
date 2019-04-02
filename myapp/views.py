
# Create your views here.
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from .forms import ProspectForm
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')
	
def response(request):
	return render(request, 'response.html')

def ProspectView(request):
	if request.method == 'POST':
		form = ProspectForm(request.POST)
		print("hello")
		if form.is_valid():
			FirstName = form.cleaned_data['yourfirst_name']
			print(FirstName)
			
	form = ProspectForm()
	
	return render(request, 'formtemplate.html', {'form': form})
 
  
  