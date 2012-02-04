from django.shortcuts import render
from forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
#from django.contrib.auth.models import User


def registration(request):
	form = RegistrationForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('index'))
			
	return render(request, 'client/registration.html', {'form': form})
	
