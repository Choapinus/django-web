from django.urls import path
from apps.team import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', views.index, name='index'),
	path('add', views.add_player, name='add_player'),
	path('delete/<int:player_id>', views.remove_player, name="remove_player"),
	path('edit/<int:player_id>', views.edit_player, name="edit_player"),
]