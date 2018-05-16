from django.shortcuts import render, redirect
from django.http import Http404
from .models import Player
from .forms import PlayerForm

# Create your views here.

def index(request):
	template_name = 'listar.html'
	context = {}
	context["players"] = Player.objects.all()
	return render(request, template_name, context)

# instalar django-bootstrap4 y buscar documentacion

def add_player(request):
	template_name = 'agregar.html'
	if request.method == 'POST':
		form = PlayerForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = PlayerForm()
	return render(request, template_name, {'form':form})

def remove_player(request, player_id):
	try:
		player = Player.objects.get(pk=player_id)
		if player.delete():
			return redirect('index')
	except Player.DoesNotExist as ex:
		raise Http404('gg larry')
	