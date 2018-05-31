from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
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
				if user.has_perm(['team.roster.Can_add_roster', ]):
					login(request, user)
					return HttpResponseRedirect(reverse('roster_coach'))
				else:
					login(request, user)
					return HttpResponseRedirect(reverse('index'))
			else:
				print("not active")
				messages.warning(
					request,
					'User inactive'
				)
		else:
			messages.error(request, 'Username or password incorrect')
	
	return render(request, template_name, context)

def logout_auth(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))

def index(request):
	template_name = 'base.html'
	context = {}
	return render(request, template_name, context)