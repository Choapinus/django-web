from django.urls import path
from apps.login import views
from django.conf import settings

urlpatterns = [
	path('', views.login_auth, name='login'),
	path('logout', views.logout_auth, name='logout'),
	path('index', views.index, name='index'),
]