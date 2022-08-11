from django.shortcuts import render

from .models import Sample
#from .forms import SampleForm


from django.urls import reverse

'''
def index(request):
	#return render(request, '')
	#return HttpResponse('<h2>hello</h2>')
	return render(request, 'index.html', {'name': 'Sample Tracker'})   
'''

def all_samples(request):
	samples= Sample.objects.all()
	return render(request, 'all_expenses.html', {'name': 'Sample Tracker', 'expenses': samples})	    
    