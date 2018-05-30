from django.urls import path
from apps.team import views
from django.conf import settings

urlpatterns = [
	path('list', views.index, name='index'),
	path('add', views.add_player, name='add_player'),
	path('delete/<int:player_id>', views.remove_player, name="remove_player"),
	path('edit/<int:player_id>', views.edit_player, name="edit_player"),
	path('roster', views.roster_view, name="roster"),
	path('roster_coach',views.roster_coach, name="roster_coach"),
	path('add_roster/<int:roster_id>',views.add_roster, name="add_roster"),
]