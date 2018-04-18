from django.contrib import admin
from apps.team.models import Team, Player, Coach, Game

# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'image_tag')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
	pass
	

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
	pass
	

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	pass