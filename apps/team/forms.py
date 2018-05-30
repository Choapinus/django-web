from django import forms
<<<<<<< HEAD
from .models import Player, Roster

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        exclude = ['id']

class RosterForm(forms.ModelForm):
	class Meta:
		model = Roster
=======
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
>>>>>>> 7426e5f8a7b2452081c4889790e679855e88424c
		fields = '__all__'
		exclude = ['id']