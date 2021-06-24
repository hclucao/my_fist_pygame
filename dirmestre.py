import os

class Diretorio:
	def __init__(self) -> None:
		"""modulo para gerenciamento de caminhos dos arquivos
		um deles é o perso(), que retorna um arquivo .png da
		spritesheet do personagem principal.
		"""
		self.diretorioMestre = os.path.dirname(__file__) #definindo os diretorio para que essa script rode em qualquer pc
		self.diretorioIMG = os.path.join(self.diretorioMestre, 'img') # aqui vamos comecar pelo diretorio principal e dps entrar na pasta img
		self.diretorioSound = os.path.join(self.diretorioMestre, 'sound')
		self.diretorioJson = os.path.join(self.diretorioMestre, 'json')

	def perso_info(self) -> None:
		return os.path.join(self.diretorioJson, 'player.json')

	def perso(self) -> None:
		return os.path.join(self.diretorioIMG, 'perso2.png')
	
	def grama(self) -> None:
		return os.path.join(self.diretorioIMG, 'grama.png')

	def soundjump(self) -> None:
		return os.path.join(self.diretorioSound, 'swm_jump.wav')

	def itens(self) -> str:
		return os.path.join(self.diretorioJson, 'itens.json')