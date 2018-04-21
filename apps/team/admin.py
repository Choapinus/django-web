from django.contrib import admin
from django.utils.html import mark_safe
from apps.team.models import Team, Player, Coach, Game

# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'image')
	search_fields = ('name', )
	readonly_fields = ['image', ]

	def image(self, obj):
		print(obj.logo.url)
		return mark_safe('<img src="{url}" />'.format(
			url = obj.logo.url
		)
	)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
	list_display = ('rut', 'name', 'nickname')
	search_fields = ['rut', 'name', 'nickname']
	list_filter = ('team', 'birthday')
	

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
	pass
	

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	pass