import pygame
import player, word

class Colider(player.Player, word.Word):
	def __init__(self):
		"""responsavel por checar colisoes
		"""
		self.playercolider()

	def playercolider(self):
		if player.playerect.colliderect(word.tilerect):
			player.gravity = False
		else: player.gravity = True
		if player.playerect.colliderect(word.blockrect):
			player.gravity = False