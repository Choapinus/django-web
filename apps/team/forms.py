from django import forms
from .models import Player, Team, Coach, Roster

class PlayerForm(forms.ModelForm):
	class Meta:
		model = Player
		fields = '__all__'
		exclude = ['id']

class Roster_playerForm(forms.ModelForm):
	class Meta:
		model = Roster
		fields = ('player',)
		exclude = ['id']
class RosterForm(forms.ModelForm):
	class Meta:
		model = Roster
		fields = '__all__'
		exclude = ['id']

class TeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = '__all__'
		exclude = ['id']

class CoachForm(forms.ModelForm):
	class Meta:
		model = Coach
		fields = '__all__'
		exclude = ['id']