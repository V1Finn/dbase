from django.shortcuts import render
from .models import dbase


 
def index(request):
	if request.method == 'POST':
		tab = dbase.objects.order_by('data')
		return render(request, 'dbase/open.html', {'dbase': tab})
	
	

	return render(request, 'dbase/index.html') 
