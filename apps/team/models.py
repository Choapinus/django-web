from django.db import models
from . import constants

# Create your models here.

class Team(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField()
	logo = models.ImageField(upload_to='img_logo')
	code = models.CharField(max_length=3)

	def __str__(self):
		return self.name

class Player(models.Model):
	name = models.CharField(max_length=200)
	nickname = models.CharField(max_length=100)
	birthday = models.DateField()
	age = models.PositiveIntegerField()
	rut = models.CharField(max_length=10)
	email = models.EmailField(max_length=254)
	height = models.FloatField()
	weight = models.FloatField()
	photo = models.ImageField(upload_to='photos')
	game_position = models.CharField(max_length=10, choices=constants.GAME_POSITIONS, default=constants.BASE)
	team = models.ForeignKey('Team', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

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