from django.urls import path
from apps.team import views
from django.conf import settings

urlpatterns = [
	# player
	path('list', views.list_player, name='list_player'),
	path('add', views.add_player, name='add_player'),
	path('delete/<int:player_id>', views.remove_player, name="remove_player"),
	path('edit/<int:player_id>', views.edit_player, name="edit_player"),

	# roster
	path('roster', views.roster_view, name="roster"),
	path('roster_coach',views.roster_coach, name="roster_coach"),
	path('add_roster_player/<int:roster_id>',views.add_roster_player, name="add_roster_player"),
	path('list_roster/<int:roster_id>', views.list_roster, name="list_roster"),
	path('add_roster',views.add_roster, name="add_roster"),

	# team
	path('list/team', views.list_team, name='list_team'),
	path('add/team', views.add_team, name='add_team'),
	path('team/delete/<int:team_id>', views.remove_team, name="remove_team"),
	path('team/edit/<int:team_id>', views.edit_team, name="edit_team"),

	# coach
	path('list/coach', views.list_coach, name='list_coach'),
	path('add/coach', views.add_coach, name='add_coach'),
	path('coach/delete/<int:coach_id>', views.remove_coach, name="remove_coach"),
	path('coach/edit/<int:coach_id>', views.edit_coach, name="edit_coach"),
]