from . import constants
from django.db import models
from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Team(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField()
	logo = models.ImageField(upload_to='img_logo')

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
	team = models.OneToOneField('Team', on_delete=models.CASCADE)
	# El equipo posee un único entrenador y cada entrenador solo puede entrenar a un único equipo.
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	perms = models.ManyToManyField(Permission)


	def __str__(self):
		return self.name

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Coach.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.coach.save()

class Game(models.Model):
	name = models.CharField(max_length=200)
	date = models.DateTimeField()
	player = models.ManyToManyField('Player')
	# Cada nómina debe contener el nombre del partido, fecha y hora y los jugadores que participaran

	def __str__(self):
		return self.name

class Roster(models.Model):
	game = models.ForeignKey('Game', on_delete=models.CASCADE)
	player = models.ManyToManyField('Player')
	coach = models.ForeignKey('Coach', on_delete=models.CASCADE)

	def __str__(self):
		return self.game.name