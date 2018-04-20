from django.db import models
from django.utils.html import format_html
from . import constants

# Create your models here.

class Team(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField()
	logo = models.ImageField()
	code = models.CharField(max_length=3)

	def __str__(self):
		return self.name

	def image(self):
		return format_html('<img src="{}" />', self.logo)

class Player(models.Model):
	name = models.CharField(max_length=200)
	nickname = models.CharField(max_length=100)
	birthday = models.DateField()
	age = models.PositiveIntegerField()
	rut = models.CharField(max_length=10)
	email = models.EmailField(max_length=254)
	height = models.FloatField()
	weight = models.FloatField()
	photo = models.ImageField()
	game_position = models.CharField(max_length=10, choices=constants.GAME_POSITIONS, default=constants.BASE)
	team = models.ForeignKey('Team', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def image(self):
		return format_html('<img src="{}" />', self.photo)

class Coach(models.Model):
	name = models.CharField(max_length=100)
	age = models.PositiveIntegerField()
	email = models.EmailField(max_length=254)
	rut = models.CharField(max_length=10)
	nickname = models.CharField(max_length=100)
	team = models.ForeignKey('Team', on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Game(models.Model):
	name = models.CharField(max_length=200)
	team = models.ForeignKey('Team', on_delete=models.CASCADE)

	def __str__(self):
		return self.name