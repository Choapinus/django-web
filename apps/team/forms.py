from django import forms
from .models import Player, Team, Coach

class PlayerForm(forms.ModelForm):
	class Meta:
		model = Player
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