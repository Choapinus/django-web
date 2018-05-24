from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def login_auth(request):
	template_name = 'login.html'
	context = {}
	user = pwd = ''

	logout(request)
	
	if request.method == 'POST':
		username = request.POST.get('user')
		pwd = request.POST.get('pwd')

		user = authenticate(username=username, password=pwd)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				messages.warning(
					request,
					'Username inactive'
				)
		else:
			messages.error(request, 'Username or password incorrect')
	
	return render(request, template_name, context)

def logout_auth(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))