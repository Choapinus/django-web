from django.contrib import admin
from django.utils.html import mark_safe
from apps.team.models import Team, Player, Coach, Game,Roster

# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'thumb', )

	def thumb(self, obj):
		return mark_safe(u'<img src="%s" style="width:70px;height:70px;"/>' \
			% (obj.logo.url))


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

@admin.register(Roster)
class RosterAdmin(admin.ModelAdmin):
	pass
