from django.contrib import admin
from apps.team.models import Team, Player, Coach, Game

# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	# list_display = ('name', 'release_date')
	# list_filter = ('id', 'name')
	# search_fields = ['name']

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
	# list_display = ('id', 'name', 'duration', 'album')

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
	# list_display = ('id', 'name', 'duration', 'album')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	# list_display = ('id', 'name', 'duration', 'album')