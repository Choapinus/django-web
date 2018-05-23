from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Player
from .forms import PlayerForm
from django.urls import reverse

def login(request):
	template_name = 'login.html'

	# return render(request, template_name, context)
	pass

def index(request):
	template_name = 'team/listar.html'
	context = {}
	context["players"] = Player.objects.all()
	return render(request, template_name, context)

# instalar django-bootstrap4 y buscar documentacion

def add_player(request):
	template_name = 'team/agregar.html'
	if request.method == 'POST':
		form = PlayerForm(request.POST or None, request.FILES)
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
		raise Http404('gg larry') # solo queria mandar el mensaje, por eso no ocupe get or 404 :c

def edit_player(request, player_id):
	template_name = 'team/agregar.html'
	player = get_object_or_404(Player, pk=player_id)
	if request.method == 'POST':
		form = PlayerForm(request.POST or None, request.FILES, instance=player)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = PlayerForm(instance=player)
	return render(request, template_name, {'form':form})




