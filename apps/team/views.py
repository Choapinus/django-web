from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Player, Roster
from .forms import PlayerForm, RosterForm, Roster_playerForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
# begin player

@login_required(login_url='login')
def list_player(request):
	# TODO: aplicar paginator
	template_name = 'player/listar.html'
	# template_name = 'base.html'
	context = {}
	context["players"] = Player.objects.all()
	return render(request, template_name, context)

# instalar django-bootstrap4 y buscar documentacion

@login_required(login_url='login')
def add_player(request):
	template_name = 'player/agregar.html'
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
	template_name = 'player/agregar.html'
	player = get_object_or_404(Player, pk=player_id)
	if request.method == 'POST':
		form = PlayerForm(request.POST or None, request.FILES, instance=player)
		if form.is_valid():
			form.save()
			return redirect('list_player')
	else:
		form = PlayerForm(instance=player)
	return render(request, template_name, {'form':form})

# end player

# begin roster

def roster_view(request):
	template_name = 'team/roster_view.html'
	data = {}
	data['rosters'] = Roster.objects.all()
	return render(request,template_name, data)

@login_required(login_url='login')
def roster_coach(request):
	template_name = 'team/roster_coach.html'
	data = {}
	data['rosters'] = Roster.objects.all()
	paginator = Paginator(data['rosters'], 10)
	page = request.GET.get('page')
	data['post'] = paginator.get_page(page)
	return render(request,template_name, data)

@login_required(login_url='login')
def add_roster_player(request, roster_id):
	template_name = "team/roster_add_player.html"
	if request.method == 'POST':
		form = Roster_playerForm(request.POST or None, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('roster_view')
	else:
		form = Roster_playerForm()
	return render(request, template_name, {'form':form})

@login_required(login_url='login')
def add_roster(request):
	template_name = "team/roster_add.html"
	if request.method == 'POST':
		form = RosterForm(request.POST or None, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('roster_view')
	else:
		form = RosterForm()
	return render(request, template_name, {'form':form})


def list_roster(request, roster_id):
	template_name = "team/roster_list_player.html"
	context = {}
	rosters = Roster.objects.get(id=roster_id)
	context['players'] = rosters

	return render(request,template_name,context)
	

# endroster

# begin team
@login_required(login_url='login')
def list_team(request):
	template_name = 'team/listar.html'
	context = {}
	context["teams"] = Team.objects.all()
	return render(request, template_name, context)

@login_required(login_url='login')
def add_team(request):
	template_name = 'team/agregar.html'
	if request.method == 'POST':
		form = TeamForm(request.POST or None, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('list_team') # change redirect
	else:
		form = TeamForm()
	return render(request, template_name, {'form':form})

@login_required(login_url='login')
def remove_team(request, team_id):
	try:
		team = Team.objects.get(pk=team_id)
		if team.delete():
			return redirect('list_team')
	except Team.DoesNotExist as ex:
		raise Http404('gg larry')

@login_required(login_url='login')
def edit_team(request, team_id):
	template_name = 'team/agregar.html'
	team = get_object_or_404(Team, pk=team_id)
	if request.method == 'POST':
		form = TeamForm(request.POST or None, request.FILES, instance=team)
		if form.is_valid():
			form.save()
			return redirect('list_team')
	else:
		form = TeamForm(instance=team)
	return render(request, template_name, {'form':form})

# end team


# begin coach

@login_required(login_url='login')
def list_coach(request):
	template_name = 'coach/listar.html'
	context = {}
	context["coachs"] = Coach.objects.all()
	return render(request, template_name, context)

@login_required(login_url='login')
def add_coach(request):
	template_name = 'coach/agregar.html'
	if request.method == 'POST':
		form = CoachForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('list_coach')
	else:
		form = CoachForm()
	return render(request, template_name, {'form':form})

@login_required(login_url='login')
def remove_coach(request, coach_id):
	try:
		coach = Coach.objects.get(pk=coach_id)
		if team.delete():
			return redirect('list_coach')
	except Coach.DoesNotExist as ex:
		raise Http404('gg larry')

@login_required(login_url='login')
def edit_coach(request, coach_id):
	template_name = 'coach/agregar.html'
	coach = get_object_or_404(Coach, pk=coach_id)
	if request.method == 'POST':
		form = CoachForm(request.POST or None, instance=coach)
		if form.is_valid():
			form.save()
			return redirect('list_coach')
	else:
		form = CoachForm(instance=coach)
	return render(request, template_name, {'form':form})

# end coach