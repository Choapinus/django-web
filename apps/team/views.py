from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Player
from .forms import PlayerForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def list_player(request):
	# TODO: aplicar paginator
	template_name = 'team/listar.html'
	# template_name = 'base.html'
	context = {}
	context["players"] = Player.objects.all()
	return render(request, template_name, context)

# instalar django-bootstrap4 y buscar documentacion

@login_required(login_url='login')
def add_player(request):
	template_name = 'team/agregar.html'
	if request.method == 'POST':
		form = PlayerForm(request.POST or None, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('list_player')
	else:
		form = PlayerForm()
	return render(request, template_name, {'form':form})

@login_required(login_url='login')
def remove_player(request, player_id):
	try:
		player = Player.objects.get(pk=player_id)
		if player.delete():
			return redirect('list_player')
	except Player.DoesNotExist as ex:
		raise Http404('gg larry') # solo queria mandar el mensaje, por eso no ocupe get or 404 :c

@login_required(login_url='login')
def edit_player(request, player_id):
	template_name = 'team/agregar.html'
	player = get_object_or_404(Player, pk=player_id)
	if request.method == 'POST':
		form = PlayerForm(request.POST or None, request.FILES, instance=player)
		if form.is_valid():
			form.save()
			return redirect('list_player')
	else:
		form = PlayerForm(instance=player)
	return render(request, template_name, {'form':form})




