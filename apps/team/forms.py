from django import forms
from .models import Player, Roster

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        exclude = ['id']

class RosterForm(forms.ModelForm):
	class Meta:
		model = Roster
		fields = '__all__'
		exclude = ['id']