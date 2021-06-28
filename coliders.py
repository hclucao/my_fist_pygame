import pygame
import player, word

class colider(player.Player, word.Word):
	def __init__(self):
		"""responsavel por checar colisoes
		"""
		self.playercolider()
		super().player.Player.player_infos()
		super().word.Word.infos()


	def playercolider(self):
		if self.rect.coliderect(self.tile):
			print("deu certo")